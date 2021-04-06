import os

def abrir(path):
    with open(path) as entrada:
        dados = entrada.read().splitlines()
        return dados

def listar_protocolos(arquivo):
    protocolos = []
    for linha in arquivo:
        if len(linha) > 500:
            if linha[0] == '1':
                if linha[457] == '3':
                    protocolos.append(linha[447:457])
        elif linha[1] == '7':
            protocolos.append(linha[1:11])
    return protocolos


def main():
    
    path_pedidos = 'F:/Projetos/DEVOLUCAO CRA/ANOS ANTERI'
    path = 'R0950512.201'

    pedidos = []
    devolvidos = listar_protocolos(abrir(path))

    for nome in os.listdir(path_pedidos):
        if 'DP095' in nome:
            caminho = os.path.join(path_pedidos, nome)
            pedidos += listar_protocolos(abrir(caminho))

    pedidos = set(pedidos)
    devolvidos = set(devolvidos)

    for item in devolvidos:
        if item not in pedidos:
            print(item)

    print(len(pedidos), len(devolvidos))

main()