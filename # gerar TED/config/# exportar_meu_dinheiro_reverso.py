import os

TED = ['BANCO DO BRASIL COMERCIAL CEN',
'CCB BRASIL                    ',
'755', 
'BANCO CITIBANK SA             ', 
'EMPRESA FORTALEZA  CE         ',
'AGENCIA PRACA DO FERREIRA CE  ']

BANCOS = [
'BANCO SANTANDER (BRASIL) S A  ', 
'INSTITUTO DE ESTUDOS DE PROTES',
'ESCRITORIO ADMINISTRATIVO IEPT',
'AGENCIA FORTALEZA             ',]

DISTRIBUIDOR = ['CARTORIO BARROS LEAL          ', 
'CARTORIO DE 2  OFICIO DE DISTR']

def abrir(path):
    with open(path, encoding='latin-1') as entrada:
        dados = entrada.read().splitlines()
        return dados

def salvar(path, dados):
    with open(path, 'w', encoding='latin-1') as saida:
        for item in dados:
            saida.write(f'{item}\n')


def formatar_data(path):
    nome = os.path.basename(path)
    dia = nome[-12:-10]
    mes = nome[-10:-8]
    ano = nome[-8:-4]
    return f'{dia}/{mes}/{ano}'


def valor_csv(dado):

    valor = float(dado.replace(',','').replace('.','')) / 100
    return '-{:.2f}'.format(valor)


def modelar_dados(dados):
    novo = []
    for item in dados:
        linha = []
        linha.append(item[43:73])
        linha.append(item[162:177])
        novo.append(';'.join(linha))
    return novo

def criar_conteudo(dados, data, csv):
    novo_csv = [csv[0]]
    for item in dados:
        csv_arr = csv[1].split(',')
        item_array = item.split(';')
        csv_arr[0] = data
        csv_arr[1] = valor_csv(item_array[1])
        if item_array[0] in TED:
            csv_arr[10] = 'DOC/TED'
        if item_array[0] not in BANCOS and item_array[0] not in TED:
            csv_arr[2] = 'Repasse Apresentante'
        if item_array[0] in DISTRIBUIDOR:
            csv_arr[2] = item_array[0]
        novo_csv.append(','.join(csv_arr))
    return novo_csv

def main():

    path_root = 'comprovantes/auto'
    opcao = input('Data do Arquivo (ex: 1902): ')

    if opcao:

        path_csv = 'config/exportar_config.csv'
        config_csv = abrir(path_csv)
        path = None

        for item in os.listdir(path_root):
            if f'{opcao}2021' in item:
                path =  f'{path_root}/{item}'

        data = formatar_data(path)
        dados = abrir(path)
        dados = modelar_dados(dados)
        novo_csv = criar_conteudo(dados, data, config_csv)
        data = data.replace('/','')
        salvar(f'{data}.csv', novo_csv)

main()