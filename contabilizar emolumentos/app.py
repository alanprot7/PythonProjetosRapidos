from modulos import *
from classes.emolumentos import Emolumentos


def main():

    app = Emolumentos()
    path = 'arquivos'
    lista_pdfs = _diretorio.listar(path)

    for item in lista_pdfs:
        arquivo = _pdf.ler(item)
        app.somar_emolumentos(arquivo) 

    print('Valor Total R$ {:.2f}*\n\n\n\n'.format(app.valor_total).replace('.',','))
    print('*valor somado apenas na coluna emolumentos, livre de Fermoju, Ferc, ISS, FAADEP e FRMMP')
     
    input()

if __name__ == '__main__':
    main()