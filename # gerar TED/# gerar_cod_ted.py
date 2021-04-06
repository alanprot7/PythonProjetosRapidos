import os
from datetime import datetime

def abrir(path):
    with open(path, encoding='latin-1') as entrada:
        dados = entrada.read().splitlines()
        return dados


def gravar(nome, dados):
    with open(nome, 'w') as saida:
        for item in dados:
            saida.write(f'{item}\n')


def mesclar_diretorio(path, data=None):
    conteudo_mesclado = []

    for item in os.listdir(path):
        if f'{data}.211' in item:
            caminho = os.path.join(path, item)
            conteudo_mesclado += abrir(caminho)
    return conteudo_mesclado


def criar_dicionario_valores(lista):
    aviso_cef = False
    valores = {}
    for item in lista:
        if item[0] == '1' and item[457] == '1':
            if item[1:4] == '104':
                aviso_cef = True
            cod = item[1:4]
            valor = int(item[260:274])
            if cod not in valores:
                valores[cod] = valor
            else:
                valores[cod] += valor
    if aviso_cef:
        print('\n{:*^50s}\n'.format('TEM PAGAMENTO DA CAIXA'))
    return valores


def criar_arquivo_cod(valores, filtro, nome):
    lista = []
    for item in valores:
        valor = valores[item]
        if item not in filtro:
            lista.append(f'{item};{valor}')
    gravar(nome, lista)


def criar_filtro():
    path = 'F:/Retornos/Contagem/ContaRetorno.ini'
    filtro = []
    for item in abrir(path):
        if item[-3:] == 'TED':
            filtro.append(item[:3]) 
    return filtro


def main():

    path = 'F:/Retornos'
    data = input('Data (ex: 01042021): ')
    
    if not data:
        now = datetime.now()
        data = now.strftime('%d%m%Y')

    nome = f'cod_{data}.txt'
    lista = mesclar_diretorio(path, data[:4])
    valores = criar_dicionario_valores(lista)
    filtro = [] #criar_filtro()
    criar_arquivo_cod(valores, filtro, nome)
    input('Concluído...')

main()