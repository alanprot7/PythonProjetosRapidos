import os

def abrir(path):
    with open(path) as entrada:
        dados = entrada.read().splitlines()
        return dados

def formata_data(data):
    dia = data[:2]
    mes = data[2:4]
    ano = data[4:]
    return f'{dia}/{mes}/{ano}'


def apresentar(item):
    print(f'Nome: {item[43:73]}')
    data = formata_data(item[93:101])
    print(f'Data: {data}')
    valor = '{:.2f}'.format(float(item[162:177]) / 100)
    print(f'Valor: R$ {valor}\n')
    return [item[162:177].strip(), item[93:101]]


def procurar(pesquisa, dados):
    novo = []
    if pesquisa:
        for item in dados:
            if item[101:104] == 'BRL' and item[230:232] == '00':
                valor = '{:.2f}'.format(float(item[162:177]) / 100)
                if pesquisa == valor:
                    novo.append(apresentar(item))
                elif pesquisa in item:
                    novo.append(apresentar(item))
    if novo:
        return novo

def localizar_arquivo(pesquisa):
    path = 'comprovantes'
    novo = []
    for root, dirs, files in os.walk(path):
        for file in files:
            arquivo = abrir(os.path.join(root, file))
            temp = procurar(pesquisa, arquivo)
            if temp:
                novo += temp
    if novo:
        return novo

def main():

    while True:

        pesquisa = input('Pequisa ou ?: ').upper().replace(',','.')

        if pesquisa == '?':
            os.system('cls')
            print('Como Pesquisar:\nDatas ex: "26022021b"\nValores ex: "1810,40"\nNomes ex: "barros leal"\nLimpar tela: "/"')
            input('...')
            os.system('cls')
        elif pesquisa == '/':
            os.system('cls')
        else:
            localizar_arquivo(pesquisa)

if __name__ == '__main__':
    main()