import os
from _consulta2 import localizar_arquivo

def abrir(path):
    with open(path, encoding='latin-1') as entrada:
        dados = entrada.read().splitlines()
        return dados

def salvar(path, lista):
    with open(path, 'w', encoding='latin-1') as saida:
        for item in lista:
            saida.write(f'{item}\n')

def comparador(pesquisa, dados):
    dados_dic = dict(dados)
    valor = pesquisa[1]
    if valor in dados_dic:
        if converter_data(pesquisa[2]) <= converter_data(dados_dic[valor]):
            return f'{pesquisa[0]};{pesquisa[1]}'

def converter_data(data):
    dia = data[:2]
    mes = data[2:4]
    ano = data[4:]
    return int(f'{ano}{mes}{dia}')

def main():

    cod = input('Lista de Repasses (ex: 26032021): ')

    path_opcao = None

    for nome in os.listdir():
        if f'{cod}.txt' in nome:
            path_opcao = nome

    if path_opcao:

        cod_values = abrir(path_opcao)
        achou_dados = False
        resultado = []

        for item in cod_values:
            item_arr = item.split(';')
            valor = float(item_arr[1].replace(',','').replace('.','')) / 100
            valor = '{:.2f}'.format(valor)
            dados = localizar_arquivo(valor)
            item_arr.append(cod)
            if dados:
                resultado.append(comparador(item_arr, dados))
        
        print('Resultado: ')
        novo_cod_values = [x for x in cod_values if x not in resultado]
        [print(x) for x in novo_cod_values]

        if len(cod_values) > len(novo_cod_values):
            sobrepor = input('Deseja Salvar?(s): ')
            if sobrepor.upper() == 'S':
                salvar(path_opcao, novo_cod_values)
                if len(novo_cod_values) == 0:
                    os.remove(path_opcao)
    
    else:
        print('Arquivo não encontrado.')

    input('...')

if __name__ == '__main__':
    main()