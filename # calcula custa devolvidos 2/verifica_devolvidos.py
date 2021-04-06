from modulos import *
from classes.devolvidos import Devolvidos
from datetime import datetime
import os


def gravar_tabela(custas, creditos):
    now = datetime.now()
    data, hora = now.strftime('%d%m%Y;%H%M%S').split(';')
    with open(f'custas_resultado/custas_{data}{hora}.csv', 'w') as saida:
        saida.write(';;LANÇAMENTOS DO PERÍODO NO EXTRATO;;;\n')
        saida.write('Data;Banco;Historico;Serie;Valor;;Emolumento;ISS;FAADEP;FRMMP;FERMOJU;Selo;Distribuidor;;Arquivo Retorno\n')
        for item in creditos:
            saida.write(f'{item}\n')
        saida.write(';;TOTAL ENTRADAS;;;\n')
        saida.write('\n\nEmolumento;ISS;FAADEP;FRMMP;FERMOJU;Selo;Distribuidor\n')
        novo = ['{:.2f}'.format(x / 100).replace('.',',') for x in custas]
        custa = ';'.join(novo)
        saida.write(custa)

def soma_custas(lista, tabela):
    soma_total = [0]
    soma_total = soma_total * 7

    for item in lista:
        for custa in tabela[1:]:
            custa_arr = [int(x) for x in custa.split(';')]
            if sum(custa_arr[:7]) == int(item):
                soma_array(soma_total, custa_arr[:7])
                break
            if sum(custa_arr) == int(item):
                soma_array(soma_total, custa_arr[:7])
                edital_arr = custa_arr[7:]
                soma_array(soma_total, edital_arr)

    return soma_total

def soma_array(soma, valores):
    for i, v in enumerate(valores):
        soma[i] += valores[i]


def load_all(path):
    diretorio = _diretorio.listar(path)
    dados = []
    for nome in diretorio:
        if _arquivo.isfile(nome):
            arquivo = _arquivo.abrir(nome)
            if '.bbt' in nome:
                arquivo = converte_bbt(arquivo)
            dados += arquivo
    return dados


def date_form(date):
    date = date.replace('/','').strip()
    dia = date[:2]
    mes = date[2:4]
    ano = date[4:]
    return int(f'{ano}{mes}{dia}')


def troca_codigo(codigo, codigos):
        for cod in codigos:
            cod_arr = cod.split(';')
            if codigo == cod_arr[0]:
                return cod_arr[1]

def processar_lista(lista, extrato):
    # extrato
    # 0 data 1 id 4 valor
    # lista
    # 0 id 1 data 2 valor

    chaves = []
    creditos = []
    for credito in lista:
        id_cred = credito.split(';')[0]
        data_cred = credito.split(';')[1]
        valor = credito.split(';')[2]
        for index, lancamento in enumerate(extrato):
            lanca_arr = lancamento.split(';')
            if len(lanca_arr) > 4:
                if valor == lanca_arr[4]:
                    if date_form(data_cred) <= date_form(lanca_arr[0]):
                        if id_cred in lanca_arr[2]:
                            chaves.append(credito)
                            creditos.append(lancamento)
                            del extrato[index]
                            break
    return [chaves, creditos, extrato]

def get_key(item):
    data = item.split(';')[0]
    return date_form(data)


def data_bbt(data):
    dia = data[:2]
    mes = data[2:4]
    ano = data[4:]
    return f'{dia}/{mes}/{ano}'

def valor_bbt(valor):
    novo = '{:.2f}'.format(int(valor) / 100)
    return novo.replace('.',',')

def converte_bbt(arquivo):
    novo = []
    for item in arquivo:
        dados = item.split(';')
        data = data_bbt(dados[3])
        serie = dados[7]
        valor = valor_bbt(dados[10])
        if dados[11] == 'D':
            valor = f'-{valor}'
        descricao = dados[12]
        novo.append(f'{data};BB;{descricao};{serie};{valor};')
    return novo

def main():

    app = Devolvidos()
    lista_base = app.abrir('F:/Retornos/Contagem/ContaRetorno.ini')
    root = 'arquivos'
    root_extratos = 'extratos'
    custas_totais = []
    if os.path.exists('lista_devolvidos.txt'):
        os.remove('lista_devolvidos.txt')

    cod_apresentantes = _arquivo.abrir('config/cod_apresentantes.txt')
    tabela = _arquivo.abrir('config/tabela.txt')
    extratos = load_all(root_extratos)
    extratos = [x.replace('.','') for x in extratos]
    extratos = [x for x in extratos if '/' in x]
    extratos = sorted(extratos, key=get_key)

    devolvidos_geral = {}
    relacao_geral_arquivos = []

    for path in os.listdir(root):
        root_path = os.path.join(root, path)
        mapa = app.processar_lista(root_path, lista_base)
        if mapa:
            for codigo in mapa:
                for nome in mapa[codigo]:
                    valor_geral = 0
                    prots_csv = []
                    for dia in mapa[codigo][nome]:
                        for protocolo in mapa[codigo][nome][dia][2]:
                            prots_csv.append(protocolo.split(';')[1])
                        valor_geral += mapa[codigo][nome][dia][1]

                    dia_mes = os.path.basename(path)[-8:-4]
                    ano = '20' + os.path.basename(path)[-3:-1]
                    ant_codigo = codigo
                    codigo = troca_codigo(codigo, cod_apresentantes)
                    indice = f'{codigo};{dia_mes}{ano}'+';{:.2f}'.format(valor_geral / 100).replace('.',',')
                    relacao_geral_arquivos.append([ant_codigo, indice, root_path])
                    devolvidos_geral[f'{indice};{root_path}'] = prots_csv


    chaves, creditos, extratos = processar_lista(devolvidos_geral, extratos)

    creditos_com_custas = []

    for index, chave in enumerate(chaves):
        custas_totais += devolvidos_geral[chave]
        custa_temp = soma_custas(devolvidos_geral[chave], tabela)
        novo = ['{:.2f}'.format(x / 100).replace('.',',') for x in custa_temp]
        custa = ';'.join(novo)
        csv = os.path.basename(chave.split(';')[-1])
        creditos_com_custas.append(f'{creditos[index]};{custa};;{csv}')


    custas = soma_custas(custas_totais, tabela)

    if creditos:
        gravar_tabela(custas, creditos_com_custas)

    falta_pagar = []
    nao_deletar = []

    arquivos_chaves = [x.split(';')[-1] for x in chaves]

    for item in relacao_geral_arquivos:
        if item[-1] not in arquivos_chaves:
            if ';0,00' not in item[1]:
                falta_pagar.append('{:60s}{}   {}'.format(item[1], item[0], item[2]))
                nao_deletar.append(_arquivo.nome(item[2]))
        else:    
            nome = _arquivo.nome(item[2])
            _arquivo.renomear(item[2], f'{root}/processados/{nome}')

    _arquivo.adicionar(f'{root_extratos}/conciliados/creditos.csv', creditos)

    for nome in _diretorio.listar(root_extratos):
        if _arquivo.isfile(nome):
            _arquivo.delete(nome)

    _arquivo.gravar(f'{root_extratos}/extratos.csv', extratos)

    
    _arquivo.gravar('falta_pagar.txt', falta_pagar)
    _arquivo.gravar('extrato_resto.txt', extratos)

    for caminho in _diretorio.listar(root):
        nome = _arquivo.nome(caminho)
        if _arquivo.isfile(caminho):
            if nome not in nao_deletar:
                _arquivo.delete(caminho)

    print('Concluído...')
    input()

if __name__ == '__main__':
    main()
