import os

class PegaProtocolos:

    def abrir(self, path):
        with open(path, encoding='latin-1') as entrada:
            dados = entrada.read().splitlines()
            return dados

    def separar(self, arquivo):
        for item in arquivo:
            if 'PROCURADORIA GERAL DO ESTADO DO CEARA' in item:
                print(item[191:198])

def main():

    app = PegaProtocolos()

    for nome in os.listdir():
        if 'BL07' in nome:
            arquivo = app.abrir(nome)
            app.separar(arquivo)

if __name__ == '__main__':
    main()