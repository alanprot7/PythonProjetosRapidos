import os

def abrir(path):
    with open(path) as entrada:
        dados = entrada.read().splitlines()
        return dados

def separar(dados):
    brasil = []
    santander = []
    for item in dados:
        dataset = item.split(';')
        if dataset[1] == 'BB':
            brasil.append(item)
        else:
            santander.append(item)
    return [brasil, santander]

def gravar(path, dados):
    with open(path, 'w', encoding='latin-1') as saida:
        for item in dados:
            saida.write(f'{item}\n')

path = 'creditos.csv'
dados = abrir(path)
brasil, santander = separar(dados)
gravar('santander.csv', santander)
gravar('brasil.csv', brasil)
os.remove(path)