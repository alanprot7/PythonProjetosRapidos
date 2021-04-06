import os

def abrir(path):
    with open(path, encoding='latin-1') as entrada:
        dados = entrada.read().splitlines()
        return dados

def mesclar_diretorio(path):
    lista_arquivos = []
    diretorio = os.listdir(path)
    for nome in diretorio:
        caminho = os.path.join(path, nome)
        lista_arquivos += abrir(caminho)
    return lista_arquivos

def gerar_lista_protocolo(lista):
    protocolos = []
    for item in lista:
        if item[0] == '1':
            protocolos.append(item[447:457])
    return protocolos


def comparar_listas(lisa1, lista2):
    for item in lisa1:
        if item not in lista2:
            print(item)

def main():
    path_enviados = 'enviados'
    path_gerados = 'gerados'

    enviados = mesclar_diretorio(path_enviados)
    gerados = mesclar_diretorio(path_gerados)

    enviados = gerar_lista_protocolo(enviados)
    gerados = gerar_lista_protocolo(gerados)

    comparar_listas(gerados, enviados)

main()