'''
document.getElementById('ptcl1').value = 1498406
valorDoCampo(1498406, 1)
novo()
document.getElementById('ptcl2').value = 1498407
valorDoCampo(1498407, 2)
novo()
document.getElementById('ptcl3').value = 1498408
valorDoCampo(1498408, 3)
'''
import os

class Renot:

    def grava(self, lista, path):
        saida = open(path, 'w', encoding='Latin-1')
        saida.write(lista[0])
        for item in lista[1:]:
            saida.write('\n' + item)
        saida.close()

    def carrega(self, path):
        entrada = open(path, 'rt', encoding='Latin-1')
        dados = entrada.read().splitlines()
        entrada.close()
        return dados

    def preparaLista(self, lista):
        novo = 'novo()'
        resultado = []
        sequencial = 1
        resultado.append(self.elaboraBoilerPlate(lista[0], sequencial))
        for item in lista[1:]:
            sequencial += 1
            resultado.append(novo)
            resultado.append(self.elaboraBoilerPlate(item, sequencial))
        return resultado

    def obtemProtocolo(self, item):
        protocolo = item.split('\t')[2]
        return protocolo

    def elaboraBoilerPlate(self, protocolo, sequencial):
        codigo = 'document.getElementById("ptcl{1}").value = {0}\nvalorDoCampo({0}, {1})'.format(protocolo, sequencial)
        return codigo

    def pegaSeteUltilmosDigitos(self, lista):
        nova_lista = list()
        for item in lista:
            protocolo = item.split('\t')[0]
            nova_lista.append(protocolo[-7:])
        return nova_lista

    def preparaListaCorreios(self, lista):
        lista_correios = self.carrega('renot_correios.txt')
        lista_correios = self.pegaSeteUltilmosDigitos(lista_correios)
        nova_lista = list()
        for item in lista:
            protocolo = self.obtemProtocolo(item)
            if not protocolo in lista_correios:
                nova_lista.append(protocolo)

        path = 'Files\\nomal.txt'
        nova_lista = self.preparaLista(nova_lista)
        self.grava(nova_lista, path)
        os.system('start ' + path)

        path = 'Files\\correios.txt'
        lista_correios = self.preparaLista(lista_correios)
        self.grava(lista_correios, path)
        os.system('start ' + path)

app = Renot()
lista = app.carrega('renot.txt')
app.preparaListaCorreios(lista)