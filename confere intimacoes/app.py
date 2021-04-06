from modulos import *
from classes.comparador import Comparador

def main():


    app = Comparador()
    path = 'arquivos'
    dia = []
    
    for item in _diretorio.listar(path):
        if '13' in item:
            dia.append(_arquivo.abrir(item))

    for item in dia[0]:
        for outro in dia[1]:
            protocolo = item[191:198]
            if outro[191:198] == protocolo:
                app.comparar_caracteres(item, outro)


if __name__ == '__main__':
    main()