from modulos import *
from classes.emolumento_com_cancelados_itau import Emolumento


def carrega_tudo(path):

    novo = []
    diretorio = _diretorio.listar(path)
    for item in diretorio:
        arquivo = _arquivo.abrir(item)
        novo += arquivo
    return novo


def main():

    path = 'arquivos'
    path_valores = 'config/valores.ini'
    path_custas = 'config/custas.csv'
    valores = _arquivo.abrir(path_valores)
    custas = _arquivo.abrir(path_custas)

    app = Emolumento(valores, custas)

    for item in _diretorio.listar(path):
        arquivo = _arquivo.abrir(item)
        resultado = app.calcula_valores(arquivo)
        nome = _arquivo.nome(item)[:-4]
        _arquivo.gravar(f'{nome}.csv', resultado)
        if app.cancelamento:
            _arquivo.gravar(f'cancelamento_{nome}.txt', app.cancelamento)
            app.cancelamento.clear()


if __name__ == '__main__':
    main()