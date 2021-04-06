from modulos import *
from classes.gera_ted2 import GeraTed

def cria_mapa(arquivo):
    mapa = [x.split(';')[0] for x in arquivo]
    return mapa

def separa_beneficiario_bb_outros(beneficiarios):
    bb = []
    outros = []
    exclusivo = []
    titularidade = []
    seg_o = []
    for ben in beneficiarios:
        ben_cod = ben.split(';')[1]
        ex_cod = ben.split(';')[0]
        documento = ben.split(';')[-2].replace('.','').replace('-','').replace('/','')

        if ex_cod == '001':
            exclusivo.append(ben)
        elif ex_cod == 'SEGO':
            seg_o.append(ben)
        elif ben_cod == '001':
            bb.append(ben)
        elif documento == '06573422000132':
            titularidade.append(ben)
        else:
            outros.append(ben)


    return [bb, outros, exclusivo, titularidade, seg_o]


def finalidade_cef(seguimento):
    chave = '1040218300000000021835'
    for index,item in enumerate(seguimento):
        if chave in item:
            part1 = item[:219]
            part2 = item[224:]
            novo = f'{part1}00014{part2}'
            seguimento[index] = novo

def header_exclusivo_bb(header):
    header[1] = header[1].replace('C20','C98')

def header_my_titularidade(header):
    header[1] = header[1].replace('C2041','C2043')

def header_seg_o(header):
    header[1] = header[1].replace('C2041','C9811')

def seq_header(app, header):
    path = 'config/seq.txt'
    seq = int(_arquivo.abrir(path)[0]) + 1
    header[0] = header[0].replace(app.mapa[24], app.comp_zeros(app.mapa[24], str(seq)))
    _arquivo.gravar(path, [str(seq)])

def valor_br(valor):
    valor_str = '{:.2f}'.format(valor)
    esquerda, direita = valor_str.split('.')
    tamanho_esq = len(esquerda)
    novo = [' ']
    for i in range(tamanho_esq * -1, 0):
        if i % 3 == 0:
            novo.append('.')
            novo.append(esquerda[i])
        else:
            novo.append(esquerda[i])
    novo = novo + [',', direita]
    return ''.join(novo).replace(' .','')


def main():

    path_modelo = 'config/modelo.txt'
    path_mapa = 'config/mapa.txt'
    path_beneficiario = 'config/beneficiarios.txt'
    path_cod = 'cod.txt'
    valor_total = 0.0
    cod = _arquivo.abrir(path_cod)
    cod = [x.replace(',','').replace('.','') for x in cod]
    
    modelo = _arquivo.abrir(path_modelo)
    mapa = cria_mapa(_arquivo.abrir(path_mapa))
    app = GeraTed(modelo, mapa)

    beneficiario = app.seleciona_beneficiario(cod, _arquivo.abrir(path_beneficiario))
    
    benefi_bb, benfi_out, exclusivo_bb, my_titula, seg_o = separa_beneficiario_bb_outros(beneficiario)

    if benfi_out:
        for index, item in enumerate(benfi_out):
            item = [item]
            header = app.cria_header_arquivo_lote()
            seq_header(app, header)
            seguimento, valor = app.cria_seguimento_ab(item)
            trailer = app.cria_trailer_arquivo_lote(len(seguimento), valor)
            finalidade_cef(seguimento)
            arquivo = header + seguimento + trailer
            path_destino = f'PG07{app.data[:-4]}_{index}.txt'
            # _arquivo.gravar(path_destino, arquivo)
            valor_total += valor / 100

    if benefi_bb:    
        for index, item in enumerate(benefi_bb):    
            item = [item]
            header = app.cria_header_arquivo_lote_bb()
            seq_header(app, header)
            seguimento, valor = app.cria_seguimento_ab(item)
            trailer = app.cria_trailer_arquivo_lote(len(seguimento), valor)
            arquivo = header + seguimento + trailer
            path_destino = f'PG07{app.data[:-4]}b_{index}.txt'
            _arquivo.gravar(path_destino, arquivo)
            valor_total += valor / 100

    if exclusivo_bb:
        for index, item in enumerate(exclusivo_bb):
            item = [item]
            header = app.cria_header_arquivo_lote_bb()
            seq_header(app, header)
            header_exclusivo_bb(header)
            seguimento, valor = app.cria_seguimento_ab(item)
            trailer = app.cria_trailer_arquivo_lote(len(seguimento), valor)
            arquivo = header + seguimento + trailer
            path_destino = f'PG07{app.data[:-4]}bb_{index}.txt'
            # _arquivo.gravar(path_destino, arquivo)
            valor_total += valor / 100

    if my_titula:
        for index, item in enumerate(my_titula):
            item = [item]
            header = app.cria_header_arquivo_lote()
            seq_header(app, header)
            header_my_titularidade(header)
            seguimento, valor = app.cria_seguimento_ab(item)
            trailer = app.cria_trailer_arquivo_lote(len(seguimento), valor)
            arquivo = header + seguimento + trailer
            path_destino = f'PG07{app.data[:-4]}my_{index}.txt'
            # _arquivo.gravar(path_destino, arquivo)
            valor_total += valor / 100

    if seg_o:
        header = app.cria_header_arquivo_lote()
        seq_header(app, header)
        header_seg_o(header)
        seguimento, valor = app.cria_seguimento_o(seg_o)
        trailer = app.cria_trailer_arquivo_lote(len(seguimento), valor)
        arquivo = header + seguimento + trailer
        path_destino = f'PG07{app.data[:-4]}BO.txt'
        # _arquivo.gravar(path_destino, arquivo)
        valor_total += valor / 100

    valor_br(valor_total)
    print('Valor total: R$' + valor_br(valor_total))
    _diferenca.verificar_diferenca(cod, valor_total)
    input()

if __name__ == '__main__':
    main()