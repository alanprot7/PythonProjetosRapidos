from modulos import *
from classes.emolumento_com_cancelados_itau_mult_tabela import Emolumento


def main():

    path = 'arquivos'
    path_valores = 'config/valores.ini'
    path_custas = 'config/custas.csv'
    path_protocolos = 'config/protocolos_tabela.ini'
    valores = _arquivo.abrir(path_valores)
    custas = _arquivo.abrir(path_custas)
    protocolos_tabela = _arquivo.abrir(path_protocolos)

    app = Emolumento(valores, custas, protocolos_tabela)

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