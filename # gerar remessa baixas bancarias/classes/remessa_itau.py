from datetime import datetime as dt

class RemessaItau:

    def __init__(self):
        self.data = dt.now().strftime('%d%m%y')
        self.id_linha_itau = '10206573422'
        self.id_linha_bb = '70206573422'
        self.header = ''.join(['01REMESSA01COBRANCA       036600964401        CARTORIO JOAO MACHADO',
            '         341BANCO ITAU SA  DATAMV                                                       ',
            '                                                                                        ',
            '                                                                                        ',
            '                                                               NUMSEQ'])

        self.trailler = ''.join(['9                                                                  ',
            '                                                                                       ',
            '                                                                                       ',
            '                                                                                       ',
            '                                                                  NUMSEQ'])

        self.linha_padrao = ''.join(['10206573422000132036600964401    0000                         ',
        '0NUMPROT0000000000000109                     I02          0000000000000000000341000',
        '0015 000000000000000000000000000000000000000000000000000000000000000000000000000000',
        '0000                                                                               ',
        '               00000000                                               000000000000 NUMSEQ'])

    def montar_base_pesquisa(self, lista):
        resultado = []
        for item in lista:
            if item[:11] == self.id_linha_itau and item[107:110] == 'I01':
                protocolo = item[63:70]
                resultado.append(protocolo)
        return resultado


    def catalogar_protocolos_sinc(self, lista):
        resultado = []
        for item in lista:
            if item[516] == '2' or item[516] == '3':
                protocolo = item[506:513]
                resultado.append(protocolo)
        return resultado


    def catalogar_protocolos_remessa(self, lista):
        resultado = []
        for item in lista:
            if item[:11] == self.id_linha_bb:
                protocolo = item[73:80]
                resultado.append(protocolo)
        return resultado


    def montar_arquivo(self, lista, protocolos):
        remessa_itau = []
        contador = 1
        remessa_itau.append(self.header.replace('DATAMV',self.data).replace('NUMSEQ', '{:06d}'.format(contador)))
        for item in lista:
            if item in protocolos:
                contador += 1
                remessa_itau.append(self.linha_padrao.replace('NUMPROT',item).replace('NUMSEQ', '{:06d}'.format(contador)))
        contador += 1
        remessa_itau.append(self.trailler.replace('NUMSEQ', '{:06d}'.format(contador)))
        return remessa_itau

        