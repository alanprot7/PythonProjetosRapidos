import os
from datetime import datetime

class CanceladosSemCusta:

    def __init__(self):
        self.now = datetime.now()
        self.excluidos = ''
        self.excluidos = self.preparaListaCra(self.excluidos)

    def carrega(self, path):
        entrada = open(path, "rt")
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def listaDiretorio(self, path):
        lista = os.listdir(path)
        lista_com_caminho = []
        
        for nome in lista:
            if '.007' in nome:
                lista_com_caminho.append(os.path.join(path,nome))

        return lista_com_caminho

    def preparaListaCra(self, lista):
        lista_protocolos = []
        for dado in lista:
            lista_protocolos.append(dado[0:10])
        return lista_protocolos

    def comparaListas(self, lista_protocolos, listaDiretorio, lista_cra):
        lista_escrita = []
        for nome_arquivo in listaDiretorio:
            arquivo = self.carrega(nome_arquivo)
            for dado in arquivo:
                if len(dado) > 457 and dado[447:448] == "7":
                    if dado[447:457] in lista_protocolos:
                        lista_protocolos.remove(dado[447:457])

        cont = 0

        if len(lista_cra) > 0:
            dia = "{:02}".format(self.now.day)
            mes = "{:02}".format(self.now.month)
            ano = "{}".format(self.now.year)
            lista_escrita.append('---------------------------------------------------------------------------------')
            lista_escrita.append('Lista de Títulos Que Faltam Baixar em {}/{}/{}'.format(dia, mes, ano))
            lista_escrita.append('---------------------------------------------------------------------------------\n')
            lista_temp = []

            for dado in lista_cra:
                if dado[0:10] in lista_protocolos and not dado[0:10] in self.excluidos:
                    lista_temp.append(dado)
            lista_temp = sorted(lista_temp)

            for dado in lista_temp:
                cont += 1
                lista_escrita.append(dado)
            lista_escrita.append('---------------------------------------------------------------------------------')
            lista_escrita.append('\nTotal: ' + str(cont) + '\n')                    

        self.grava(lista_escrita)

    def grava(self, lista):
        saida = open('FaltaCancelar.txt', 'w')
        for dado in lista:
            saida.write(dado + '\n')
        saida.close()
        os.system('start FaltaCancelar.txt')

def lista_novos(path):
    app = CanceladosSemCusta()
    novo = []
    for root, dirs, files in os.walk(path):
        for file in files:
            caminho = os.path.join(root, file)
            arquivo = app.carrega(caminho)
            novo += arquivo
    return novo

def main():

    app = CanceladosSemCusta()
    print('Aguarde...')
    lista_diretorio = app.listaDiretorio("F:/Projetos/Retorno Dist")
    lista_cra = lista_novos('Anos')
    lista_protocolos = app.preparaListaCra(lista_cra)
    app.comparaListas(lista_protocolos, lista_diretorio, lista_cra)


if __name__ == "__main__":
    main()