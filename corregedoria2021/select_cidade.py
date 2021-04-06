def abrir(path):
    with open(path, encoding='latin-1') as entrada:
        dados = entrada.read().splitlines()
        return dados

def salvar(path, lista):
    with open(path, 'w', encoding='latin-1') as saida:
        for i in lista:
            saida.write(f'{i}\n')


def processar_nova_lista(lista, limite):
    novo = []
    contador = {}
    for i in lista:
        dado = i.split(';')[-1]
        if dado not in contador:
            contador[dado] = 0
        contador[dado] += 1
        if dado in limite:
            if contador[dado] <= limite[dado]:
                novo.append(i)
        else:
            novo.append(i)
    return novo


def main():

    path = 'novo_apontados.csv'

    arquivo = abrir(path)
    cidades = {}
    limite = {}
    for i in arquivo:
        cidade = i.split(';')[-1]
        if cidade not in cidades:
            cidades[cidade] = 0
        cidades[cidade] += 1

    for i in cidades:
        if cidades[i] > 15:
            limite[i] = cidades[i] - int(cidades[i] * 0.2035)

    nova_lista = processar_nova_lista(arquivo, limite)
    print(len(arquivo), len(nova_lista))
    salvar('novo_apontados_filtro.csv', nova_lista)

if __name__ == '__main__':
    main()