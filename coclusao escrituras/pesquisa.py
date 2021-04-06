import os

def abrir(path):
    with open(path, encoding='latin-1') as entrada:
        dados = entrada.read().splitlines()
        return dados

def procurar(lista, arquivo):
    cont = 0
    for item in lista:
        nao_achou = True
        for arq in arquivo:
            if item in arq:
                nao_achou = False
        if nao_achou:
            print(item)
            cont += 1
    print(cont)


path = 'F:/Projetos/XPROGs/livro_diario_auxiliar/processados'
lista = abrir('data.txt')

arquivos = []

for root, dirs, files in os.walk(path):
    for file in files:
        caminho = os.path.join(root, file)
        if 'DeclaracaoSisguia' in caminho:
            arquivos += abrir(caminho)

procurar(lista, arquivos)
