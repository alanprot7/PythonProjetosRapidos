from modulos import *
from classes.baixas import Baixas


def load_all(path):
    novo = []
    diretorio = _diretorio.listar(path)
    for caminho in diretorio:
        if '.txt'.upper() in caminho.upper():
            arquivo = _arquivo.abrir(caminho)
            novo += arquivo
    return novo

def main():

    app = Baixas()
    path_baixas = 'arquivos/baixas'
    path_remessas = 'arquivos/remessas'
    baixas = load_all(path_baixas)
    remessas = load_all(path_remessas)
    prots_remessas = app.pega_protocolo_remessa(remessas)
    prots_baixas = app.pega_protocolo_baixa(baixas)
    renotificar = app.gera_lista_renotificar(prots_baixas, prots_remessas)
    renotificar  = sorted(list(set(renotificar)))
    _arquivo.gravar('renotificar.txt', renotificar)
    print('remessas', len(prots_remessas))
    print('renotificar', len(renotificar))
    print('Ativos', len(prots_remessas) - len(renotificar))
    ativos = sorted(app.diferenca(prots_remessas, renotificar))
    _arquivo.gravar('ativos.txt', ativos)
    input()

if __name__ == '__main__':
    main()