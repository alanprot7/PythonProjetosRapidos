def abrir(path):
    with open(path, encoding='latin-1') as entrada:
        dados = entrada.read().splitlines()
        return dados

def main():

    path = 'novo_protestados.csv'

    arquivo = abrir(path)

    result = [x for x in arquivo if len(x.split(';')) < 7]

    [print(x) for x in result]
    print(len(result))

main()