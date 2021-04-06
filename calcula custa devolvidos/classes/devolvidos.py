class Devolvidos:

    def abrir(self, path):
        with open(path, encoding='latin-1') as entrada:
            dados = entrada.read().splitlines()
            return dados

    def montar_mapa(self, lista):
        mapa = {}
        codigo = lista[0][1:4]
        nome = lista[0][4:43]
        for item in lista[1:-1]:
            status = item[457:458]
            if status == '3' or status == '4':
                data = item[477:485]
                protocolo = item[447:457]
                if not codigo in mapa:
                    mapa[codigo] = {}
                    mapa[codigo][nome] = {}
                if not data in mapa[codigo][nome]:
                    mapa[codigo][nome][data] = [1, int(item[471:476]),[f'{protocolo};{item[471:476]}']]
                else:
                    valor = int(item[471:476])
                    mapa[codigo][nome][data][0] += 1
                    mapa[codigo][nome][data][1] += valor
                    mapa[codigo][nome][data][2].append(f'{protocolo};{valor}')
        return mapa

    def processar_lista(self, path, lista_base):
        for item in lista_base:
            codigo = item.split(' ')[0]
            meio = item.split(' ')[-1]
            if meio == 'TED':
                if 'R' + codigo in path:
                    arquivo = self.abrir(path)
                    mapa = self.montar_mapa(arquivo)
                    return mapa

    def gravar(self, linha):
        with open('lista_devolvidos.txt', 'a') as saida:
            saida.write(linha + '\n')
