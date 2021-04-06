import os

IGNORADOS = ['074','488','771']

def abrir(path):
    with open(path, encoding='latin-1') as entrada:
        dados = entrada.read().splitlines()
        return dados

def salvar(path, lista):
    with open(path, 'a', encoding='latin-1') as saida:
        for item in lista:
            saida.write(f'{item}\n')

def criar_lista_protocolos(path):
    arquivo = abrir(path)
    novo = {}
    for item in arquivo:
        chave = item[457:458]
        protocolo = item[447:457]
        codigo = item[1:4]
        if chave == '1' and codigo not in IGNORADOS:
            novo[protocolo] = None
        if chave == 'G':
            valor = float(item[260:274]) / 100
            novo[protocolo] = '{:12.2f}'.format(valor).replace('.',',')
    return novo

def eliminar_ja_pagos(distribuidor, retornos):
    for retorno in retornos:
        if retorno in distribuidor:
            del distribuidor[retorno]

def listar_data(data, path):
    if '21.007' in path:
        if f'BA{data}' in path:
            return True
    return False

def main():

    path_retorno = 'F:/Retornos'
    path_distribuidor = 'F:/Projetos/Retorno Dist'
    
    while True:

        opcao = input('Informe Data (ex: 2402): ')

        retornos = []
        distribuidor = None

        for item in os.listdir(path_retorno):
            caminho = os.path.join(path_retorno, item)
            if '.211' in caminho:
                retornos += criar_lista_protocolos(caminho)

        for item in os.listdir(path_distribuidor):
            caminho = os.path.join(path_distribuidor, item)
            if listar_data(opcao, caminho):
                distribuidor = criar_lista_protocolos(caminho)

        if distribuidor:
            eliminar_ja_pagos(distribuidor, retornos)

        nova_lista = [f'{x}\t{distribuidor[x]}' for x in distribuidor]

        resultado = [f'Resultado dia {opcao}21',''] + nova_lista + ['']

        salvar('resultado.txt', resultado)
        [print(x) for x in resultado]
        input()
        os.system('cls')

main()