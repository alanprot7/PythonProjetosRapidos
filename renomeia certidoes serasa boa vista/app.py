from modulos import *
from classes.certidao import Certidao

def main():

    app = Certidao()
    path = 'F:/Projetos/XPROGs/RECIBO-SERASA/Certidoes'
    lista = _diretorio.listar(path)
    for item in lista:
        if '32CERTSERBV' in item:
            arquivo = _pdf.ler(item)
            destino = app.trazer_destino(arquivo)
            data = app.trazer_data(arquivo)
            ato = app.trazer_ato(arquivo)
            novo_nome = '{}{}_{}.pdf'.format(destino,ato,data)
            nome = _arquivo.nome(item)
            _arquivo.renomear(item, item.replace(nome, novo_nome))


if __name__ == '__main__':
    main()