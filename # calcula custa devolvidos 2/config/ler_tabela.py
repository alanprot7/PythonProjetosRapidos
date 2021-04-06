def abrir(path):
    with open(path) as entrada:
        dados = entrada.read().splitlines()
        return dados
[print(x) for x in abrir('tabela.txt')]
input()