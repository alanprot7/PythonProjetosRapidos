import os


def abrir(path):
    with open(path, encoding='latin-1') as entrada:
        dados = entrada.read().splitlines()
        return dados


def gravar(path, dados):
    with open(path, 'w', encoding='latin-1') as saida:
        for item in dados:
            saida.write(item + '\n')


def adicionar(path, dados):
    with open(path, 'a', encoding='latin-1') as saida:
        for item in dados:
            saida.write(item + '\n')


def renomear(path, novo_path):
    os.rename(path, novo_path)


def exite(path):
    return os.path.exists(path)


def nome(path):
    return os.path.basename(path)


def isfile(path):
    return os.path.isfile(path)

def delete(path):
    os.remove(path)