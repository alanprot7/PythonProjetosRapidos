from modulos import *

def main():

    path = 'vencidos.csv'
    arquivo = _arquivo.abrir(path)

    protocolos = [item.split(';')[4][2:-1] for item in arquivo]

    novo = []

    for protocolo in protocolos:
        linha = '{0:>513s}{1:>4s}{1:100s}'.format(protocolo, '3')
        novo.append(linha)

    _arquivo.gravar('novo.txt', novo)

if __name__ == '__main__':
    main()