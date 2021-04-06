class Kennerson:

    def abrir(self, path):
        with open(path, encoding='latin-1') as entrada:
            dados = entrada.read().splitlines()
            return dados

    def procurar(self, arquivo):
        for item in arquivo:
            if item[457] == '2':
                print('Protestado', item[447:457], 'Data', item[477:485])

def main():
    app = Kennerson()

    path = 'R1482704.201'

    arquivo = app.abrir(path)

    app.procurar(arquivo)


if __name__ == '__main__':
    main()