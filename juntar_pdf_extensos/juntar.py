from modulos import *

path_pdfs = 'D:/rapi'
path_gravar = 'lista.txt'

lista = _diretorio.listar(path_pdfs)

_arquivo.gravar(path_gravar, lista)

_pdf.juntar(path_gravar)