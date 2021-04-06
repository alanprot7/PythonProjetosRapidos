def abrir(path):
    with open(path) as entrada:
        dados = entrada.read().splitlines()
        return dados

def formata_valor(valor):
    global valor_total
    float_valor = float(valor) / 100
    valor_total+= float_valor
    return '{:13.2f}'.format(float_valor).replace('.',',')

def formata_data(data):
    dia = data[:2]
    mes = data[2:4]
    ano = data[4:]
    return f'  {dia}/{mes}/{ano}'

def listar_protocolos(arquivo):
    novo = []
    for item in arquivo:
        if item[457] == '3':
            novo.append([item[447:457],formata_data(item[477:487]),formata_valor(item[471:476])])
    return novo

valor_total = 0.0

def main():

    path = 'R0950512.202'
    arquivo = abrir(path)
    lista = listar_protocolos(arquivo)
    [print(*x) for x in lista]
    print('{:.2f}'.format(valor_total))

main()