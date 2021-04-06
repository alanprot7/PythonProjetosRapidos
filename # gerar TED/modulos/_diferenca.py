def verificar_diferenca(arquivo, valor_total):
    valor_arquivo = sum([float(x.split(';')[1]) for x in arquivo]) / 100
    valor_arquivo = float('{:.2f}'.format(valor_arquivo))
    valor_total = float('{:.2f}'.format(valor_total))

    if valor_total != valor_arquivo:
        valor_diferenca = valor_arquivo - valor_total
        print('Diferença R$: {:.2f}'.format(valor_diferenca))