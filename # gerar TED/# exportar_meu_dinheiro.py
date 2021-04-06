import os

TED = ['001','320','755', '745', '104']
DISTRIBUIDOR = {'1OFICIO':'CARTORIO BARROS LEAL          ', 
'2OFICIO':'CARTORIO DE 2  OFICIO DE DISTR'}

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


def criar_conteudo(dados, data, csv):
    novo_csv = [csv[0]]
    for item in dados:
        csv_arr = csv[1].split(',')
        item_array = item.split(';')
        csv_arr[0] = data
        csv_arr[1] = valor_csv(item_array[1])
        nome = item_array[0]
        if nome in TED:
            csv_arr[10] = 'DOC/TED'
        if len(nome) > 3:
            csv_arr[2] = 'Repasse Apresentante'
        if nome in DISTRIBUIDOR:
            csv_arr[2] = DISTRIBUIDOR[nome]
        novo_csv.append(','.join(csv_arr))
    return novo_csv

def main():

    opcao = input('Data do Arquivo (ex: 1902): ')

    if opcao:

        path_csv = 'config/exportar_config.csv'
        config_csv = abrir(path_csv)
        path = None

        for item in os.listdir():
            if f'{opcao}2021.txt' in item:
                path = item

        data = formatar_data(path)
        dados = abrir(path)
        novo_csv = criar_conteudo(dados, data, config_csv)
        data = data.replace('/','')
        salvar(f'{data}.csv', novo_csv)

main()