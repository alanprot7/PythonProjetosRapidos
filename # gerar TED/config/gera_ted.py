from datetime import datetime
# now = datetime.now()
# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

class GeraTed:

    def __init__(self, modelo, mapa):
        now = datetime.now()
        self.data, self.hora = now.strftime('%d%m%Y;%H%M%S').split(';')
        self.modelo = modelo
        self.mapa = mapa

    def cria_header_arquivo_lote(self):
        header = [self.modelo[0].replace(self.mapa[0],self.data).replace(self.mapa[1],self.hora)]
        header.append(self.modelo[1])
        return header


    def cria_header_arquivo_lote_bb(self):
        header = [self.modelo[0].replace(self.mapa[0],self.data).replace(self.mapa[1],self.hora)]
        header.append(self.modelo[1].replace('00100011C2041007','00100011C2001007'))
        return header


    def cria_trailer_arquivo_lote(self, seq, valor):
        seq += 2
        trailer = [self.modelo[4]]
        trailer.append(self.modelo[5])
        trailer[0] = trailer[0].replace(self.mapa[16], self.comp_zeros(self.mapa[16], str(seq)))
        trailer[0] = trailer[0].replace(self.mapa[17], self.comp_zeros(self.mapa[17], str(valor)))
        seq += 2
        trailer[1] = trailer[1].replace(self.mapa[18], self.comp_zeros(self.mapa[18], str(seq)))

        return trailer


    def cria_seguimento_ab(self, beneficiario):
        especiais = ['.','/','-']
        valor_total = 0
        conteudo = []
        cont = 1
        for item in beneficiario:
            ben = item.split(';')
            segA = self.modelo[2]
            segB = self.modelo[3]
            segA = segA.replace(self.mapa[2],self.comp_zeros(self.mapa[2], str(cont)))
            segA = segA.replace(self.mapa[3],ben[1])
            segA = segA.replace(self.mapa[4],self.comp_zeros(self.mapa[4], ben[2]))
            segA = segA.replace(self.mapa[5],ben[3])
            segA = segA.replace(self.mapa[6],self.comp_zeros(self.mapa[6], ben[4]))
            segA = segA.replace(self.mapa[7],ben[5])
            segA = segA.replace(self.mapa[8],self.comp_espacos(self.mapa[8], ben[6].upper()))
            segA = segA.replace(self.mapa[9],self.data)
            segA = segA.replace(self.mapa[10],self.comp_zeros(self.mapa[10], ben[9]))
            segA = segA.replace(self.mapa[11],self.data)
            segA = segA.replace(self.mapa[12],self.comp_zeros(self.mapa[12], ben[9]))
            cont += 1
            segB = segB.replace(self.mapa[13],self.comp_zeros(self.mapa[13], str(cont)))
            segB = segB.replace(self.mapa[14],ben[7])
            for s in especiais:
                ben[8] = ben[8].replace(s,'')
            segB = segB.replace(self.mapa[15],self.comp_espacos(self.mapa[15],ben[8]))
            valor_total += int(ben[9])
            cont += 1
            conteudo.append(segA)
            conteudo.append(segB)
        return [conteudo, valor_total]


    def seleciona_beneficiario(self, cod, beneficiario):
        novo = []
        for c_banco in cod:
            cod_arr = c_banco.split(';')
            for item in beneficiario:
                ben = item.split(';')[0]
                if cod_arr[0] == ben:
                    novo.append(f'{item};{cod_arr[1]}')
        return novo

    def comp_zeros(self, cod, dado):
        zeros = '0' * (len(cod) - len(dado))
        novo = zeros + dado
        return novo

    def comp_espacos(self, cod, dado):
        if len(dado) > len(cod):
            dado = dado[:len(cod)]
        espaco = ' ' * (len(cod) - len(dado))
        novo = dado + espaco
        return novo
