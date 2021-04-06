from modulos import *
from app import listar_conteudo_arquivos as load

def catalogar_protocolos_sinc(lista):
    resultado = []
    codigos = ['1','2','3']
    for item in lista:
        if item[516] in codigos:
            protocolo = item[506:513]
            resultado.append(protocolo)
    return resultado


def main():

    path_sinc = 'sinc'
    sinc = set(catalogar_protocolos_sinc(load(path_sinc)))
    base = set([item[:7] for item in _arquivo.abrir('base.txt') if int(item[:7]) < 1600000])
    [sinc.add(item) for item in _arquivo.abrir('base_del.txt')]
    _arquivo.gravar('reimp.txt', [item for item in base if item not in sinc])


if __name__ == '__main__':
    main()
