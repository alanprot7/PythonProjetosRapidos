def date_int(date):
    new = date.replace('/','').strip()
    day = new[:2]
    month = new[2:4]
    year = new[-4:]
    return int(f'{year}{month}{day}')


def abrir(path):
    with open(path) as entrada:
        dados = entrada.read().splitlines()
        return dados


path_resto = 'extrato_resto.txt'
path_falta = 'falta_pagar.txt'

resto = abrir(path_resto)
falta = abrir(path_falta)

for lancamento in falta:
    resultado = []
    valor = lancamento.split(';')[2][:10].strip()
    data = date_int(lancamento.split(';')[1].strip())
    for entrada in resto:
        data_entrada = date_int(entrada.split(';')[0].strip())
        if valor in entrada:
            if data <= data_entrada:
                resultado.append(entrada)

    if resultado:
         print('\n',lancamento,'\n------------------------')
         [print(x) for x in resultado]

input('Concluido...')