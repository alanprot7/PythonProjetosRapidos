import os

# passar arquivo para ler no path

def ler(path, opcao = '-l'):
    path_novo = '"' + path + '"'
    proc = os.popen('java -jar modulos/pdf2.jar ' + path_novo + ' ' + opcao)
    dados = proc.read().splitlines()
    return dados

# passar o path por parametro e ele gera as paginas no mesmo nome com numeros, mantem original

def separar(path, opcao = '-s'):
    path_novo = '"' + path + '"'
    proc = os.popen('java -jar modulos/pdf2.jar ' + path_novo + ' ' + opcao)
    dados = proc.read().splitlines()
    return dados

# passar aquivo .txt com lista de arquivos no path, gera merge-pdf-result.pdf

def juntar(path, opcao = '-j'):
    path_novo = '"' + path + '"'
    proc = os.popen('java -jar modulos/pdf2.jar ' + path_novo + ' ' + opcao)
    dados = proc.read().splitlines()
    return dados
