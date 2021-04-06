import os


def abrir(path):
    with open(path, encoding='latin-1') as entrada:
        dados = entrada.read().splitlines()
        return dados

def salvar(path, lista):
    with open(path, 'w', encoding='latin-1') as saida:
        for item in lista:
            saida.write(f'{item}\n')

def data_br(data):
    dia = data[:2]
    mes = data[2:4]
    ano = data[4:]
    return f'{dia}/{mes}/{ano}'

def normalizar_cancelamento(lista):
    cabecalho = lista[0].split(';')
    del lista[0]
    cabecalho.insert(3, 'CANCELADO')
    for i,item in enumerate(lista):
        arr = item.split(';')
        arr.insert(3, ' - ')
        lista[i] = ';'.join(arr)
    lista.insert(0, ';'.join(cabecalho))

def normalizar_protesto(lista):
    cabecalho = lista[0].split(';')
    del lista[0]
    cabecalho.insert(2, 'PROTESTO')
    for i,item in enumerate(lista):
        arr = item.split(';')
        arr.insert(2, ' - ')
        lista[i] = ';'.join(arr)
    lista.insert(0, ';'.join(cabecalho))

def numerar_linhas(lista):
    cabecalho = lista[0].split(';')
    del lista[0]
    cabecalho.insert(0, 'N° LINHA')
    for i,item in enumerate(lista):
        arr = item.split(';')
        arr.insert(0, str(i + 1))
        lista[i] = ';'.join(arr)
    lista.insert(0, ';'.join(cabecalho))

def inserir_situacao(lista):
    pos = 5
    cabecalho = lista[0].split(';')
    del lista[0]
    cabecalho.insert(pos, 'SITUAÇÃO ATUAL')
    for i,item in enumerate(lista):
        arr = item.split(';')
        if arr[3] != ' - ':
            arr.insert(pos, 'Cancelado')
        elif arr[2] != ' - ':
            arr.insert(pos, 'Protestado')
        else:
            arr.insert(pos, 'Apontado')
        lista[i] = ';'.join(arr)
    lista.insert(0, ';'.join(cabecalho))

def inserir_situacao_plus(lista):
    pos = 7
    cabecalho = lista[0].split(';')
    del lista[0]
    cabecalho.insert(pos, 'SITUAÇÃO ATUAL')
    for i,item in enumerate(lista):
        arr = item.split(';')
        if arr[6] != '-':
            arr.insert(pos, 'Sustado')
        elif arr[5] != '-':
            arr.insert(pos, 'Devolvido')
        elif arr[4] != '-':
            arr.insert(pos, 'Pago')
        elif arr[3] != '-':
            arr.insert(pos, 'Cancelado')
        elif arr[2] != '-':
            arr.insert(pos, 'Protestado')
        else:
            arr.insert(pos, 'Apontado')
        lista[i] = ';'.join(arr)
    lista.insert(0, ';'.join(cabecalho))

def update_cancelamento(protestos, protocolos):
    for i,item in enumerate(protestos):
        arr = item.split(';')
        if arr[0]:
            if arr[0] in protocolos:
                data_cancelamento = data_br(protocolos[arr[0]][1])
                arr[3] = data_cancelamento
                protestos[i] = ';'.join(arr)

def update_protesto(apontados, protocolos):
    for i,item in enumerate(apontados):
        arr = item.split(';')
        if arr[0]:
            if arr[0] in protocolos:
                data_cancelamento = data_br(protocolos[arr[0]][0])
                arr[2] = data_cancelamento
                apontados[i] = ';'.join(arr)


def catalogar_serasa(path):
    ext = ['.FLA', '.TXT']
    lista = []
    for root, dirs, files in os.walk(path):
        for file in files:
            path_file = os.path.join(root, file)
            extension = os.path.splitext(path_file)[-1]
            if extension.upper() in ext:
                lista.append(path_file)
    return lista

def listar_protocolos(lista):
    cancelamentos = {}
    protestos = {}
    for nome in lista:
        arquivo = abrir(nome)
        for item in arquivo:
            if '1CECEFLA' in item:
                protocolo = int(item[447:457])
                if protocolo > 775363 and protocolo < 1182090:
                    cancelamentos[str(protocolo)] = ['', item[477:485]]
            if '1PICEFLA' in item:
                protocolo = int(item[447:457])
                if protocolo > 775363 and protocolo < 1182090:
                    protestos[str(protocolo)] = [item[260:268], '']

    return cancelamentos, protestos

def processar_uma_etapa(arquivo, cancels):

    normalizar_cancelamento(arquivo)
    update_cancelamento(arquivo, cancels)
    #inserir_situacao(arquivo)
    
def processar_duas_etapas(arquivo, prots, cancels):

    normalizar_protesto(arquivo)
    update_protesto(arquivo, prots)
    processar_uma_etapa(arquivo, cancels)
   
def gerar_listas_caminhos(path):
    caminhos = []
    for item in os.listdir(path):
        caminho = os.path.join(path, item)
        caminhos.append(caminho)
    return caminhos

def main():

    path_serasa = 'F:/Projetos/Serasa'
    path_uma_etapa = 'arquivos/uma_etapa'
    path_duas_etapas = 'arquivos/duas_etapas'

    # serasa = catalogar_serasa(path_serasa)
    # cancels, prots = listar_protocolos(serasa)

    # uma_etapa = gerar_listas_caminhos(path_uma_etapa)
    # duas_etapas = gerar_listas_caminhos(path_duas_etapas)

    # for path in uma_etapa:
    #     arquivo = abrir(path)
    #     processar_uma_etapa(arquivo, cancels)
    #     path = 'processados/' + os.path.basename(path)
    #     salvar(f'{path}', arquivo)

    # for path in duas_etapas:
    #     arquivo = abrir(path)
    #     processar_duas_etapas(arquivo, prots, cancels)
    #     path = 'processados/' + os.path.basename(path)
    #     salvar(f'{path}', arquivo)    
 
    path_numerar = 'arquivos/numerar'
    numerar =  gerar_listas_caminhos(path_numerar)
    
    for path in numerar:
        arquivo = abrir(path)
        inserir_situacao_plus(arquivo)
        numerar_linhas(arquivo)
        path = 'processados/' + os.path.basename(path)
        salvar(f'{path}', arquivo)   


if __name__ == '__main__':
    main()