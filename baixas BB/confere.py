from modulos import *

def main():

    retorno = _arquivo.abrir('CBR643413006202012658.ret')
    ativos = _arquivo.abrir('ativos.txt')

    prot_retorno = [item[73:80] for item in retorno if item[108:110] == '14']
    diferenca = [item for item in ativos if item not in prot_retorno]
    print(diferenca)

if __name__ == '__main__':
    main()
