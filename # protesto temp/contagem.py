import os

class Contagem:

    def __init__(self, booleano):
        self.selecao = booleano

    def abrir(self, path):
        with open(path, encoding='Latin-1') as entrada:
            dados = entrada.read().splitlines()
        return dados

    def salvar(self, path, lista):
        with open(path, 'w', encoding='Latin-1') as saida:
            for item in lista:
                saida.write(item + '\n')

    def listar_protocolos(self, lista, base):
        dados = set()
        for item in lista:
            somente_base = self.selecao
            for item_base in base:
                if item_base in item:
                    somente_base = not somente_base
            if not somente_base:
                dados.add(item)
        return dados

    def salvar_lista(self, lista):
        novo = []
        for item in lista:
            novo.append(item)
        novo.append(str(len(lista)))
        self.salvar('resultado.txt',novo)

    def getKey(self, item):
        return item[:7]


opcao = bool(int(input('(1) base (0) Outros: ')))


app = Contagem(opcao)
path_protocolos = 'protocolos.txt'
path_base = 'base.txt'
path_prot_base = 'D:/Google Drive/Python/Projetos Rápidos/sindicado cofeccoes/prot_base.txt'
path_pedidos = 'D:/Google Drive/Python/Projetos Rápidos/sindicado cofeccoes/pedidos.txt'

lista = app.abrir(path_protocolos)
base = app.abrir(path_base)

base += app.abrir(path_prot_base)

print(len(base))

pedidos = [item[:7] for item in app.abrir(path_pedidos)]

base = [item for item in base if item not in pedidos]

print(len(base))

protocolos = app.listar_protocolos(lista, base)

protocolos = sorted(protocolos, key=app.getKey)

app.salvar_lista(protocolos)

os.system('start resultado.txt')

input()