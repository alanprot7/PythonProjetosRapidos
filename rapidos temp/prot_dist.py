import os


def abrir(path):
    with open(path, encoding='latin-1') as entrada:
        dados = entrada.read().splitlines()
        return dados

def pesquisar(dado, arquivo):
    for item in arquivo:
        if dado in item:
            print('Achado', arquivo[0][44:52])

def main():

    path = 'F:/Projetos/Retorno Dist'

    for root, dirs, files in os.walk(path):
        for file in files:
            if '.007' in file:
                caminho = os.path.join(root, file)
                arquivo = abrir(caminho)
                pesquisar('7205715846', arquivo)
    input()

if __name__ == '__main__':
    main()