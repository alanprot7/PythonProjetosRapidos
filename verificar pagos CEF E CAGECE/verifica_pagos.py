import os

class VerificaPagos:

    def abrir(self, path):
        with open(path, encoding='latin-1') as entrada:
            dados = entrada.read().splitlines()
            return dados

    def montar_mapa(self, lista):
        mapa = {}
        codigo = lista[0][1:4]
        nome = lista[0][4:43]
        for item in lista[1:-1]:
            if item[457:458] == '1':
                data = item[477:485]
                protocolo = item[447:457]
                if not codigo in mapa:
                    mapa[codigo] = {}
                    mapa[codigo][nome] = {}
                if not data in mapa[codigo][nome]:
                    mapa[codigo][nome][data] = [1, int(item[260:274]),[protocolo]]
                else:
                    valor = int(item[260:274])
                    mapa[codigo][nome][data][0] += 1
                    mapa[codigo][nome][data][1] += valor
                    mapa[codigo][nome][data][2].append(protocolo)
        return mapa

    def processar_lista(self, path):
        if 'R' in path:
            arquivo = self.abrir(path)
            mapa = self.montar_mapa(arquivo)
            return mapa

    def gravar(self, linha):
        with open('lista_pagamentos.txt', 'a') as saida:
            saida.write(linha + '\n')

def main():
    app = VerificaPagos()
    root = 'arquivos'
    geral_geral = 0
    for path in os.listdir(root):
        root_path = os.path.join(root, path)
        mapa = app.processar_lista(root_path)
        if mapa:
            for codigo in mapa:
                for nome in mapa[codigo]:
                    valor_geral = 0
                    app.gravar(f'Arquivo: {os.path.basename(path)}')
                    app.gravar(codigo + ' ' + nome)
                    print(codigo + ' ' + nome)
                    for dia in mapa[codigo][nome]:
                        for protocolo in mapa[codigo][nome][dia][2]:
                            app.gravar(protocolo)
                        app.gravar ('{} {} {:.2f}'.format(dia, 
                        mapa[codigo][nome][dia][0], 
                        (mapa[codigo][nome][dia][1] / 100)))
                        app.gravar('-------------------')
                        valor_geral += mapa[codigo][nome][dia][1]
                    geral_geral += valor_geral
                    print('TOTAL ======== {:.2f}'.format(valor_geral / 100).replace('.',','))
    app.gravar('TOTAL GERAL R$ {}'.format(geral_geral /100))
    app.gravar(f'\n\n')
    input('Concluído...')
if __name__ == '__main__':
    main()
