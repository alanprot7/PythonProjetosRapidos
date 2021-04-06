from classes.remessa_itau import RemessaItau

class RemessaBB(RemessaItau):

    def __init__(self):
        super().__init__()
        self.header_bb = ''.join(['01REMESSA01COBRANCA       13692009801197000000CARTORIO JOAO MACHADO',
            '         001BANCODOBRASIL  DATAMV0000038                      3253391                    ',
            '                                                                                         ',
            '                                                                                         ',
            '                                                            NUMSEQ'])


    def catalogar_linhas_remessa(self, lista):
        resultado = []
        for item in lista:
            if item[:11] == self.id_linha_bb:
                linha = item
                resultado.append(linha)
        return resultado


    def montar_arquivo_bb(self, lista_baixar, lista_linhas, protocolos):
        remess_bb = []
        contador = 1
        remess_bb.append(self.header_bb.replace('DATAMV',self.data).replace('NUMSEQ', '{:06d}'.format(contador)))
        for baixa in lista_baixar:
            if baixa in protocolos:
                for item in lista_linhas:
                    if item[73:80] == baixa:
                        contador += 1
                        remess_bb.append(self.formata_linha(item) + '{:06d}'.format(contador))
        contador += 1
        remess_bb.append(self.trailler.replace('NUMSEQ', '{:06d}'.format(contador)))
        return remess_bb


    def formata_linha(self, linha):
        part1 = linha[:108]
        part2 = linha[110:158]
        part3 = linha[160:394]
        novo = '{}02{}44{}'.format(part1, part2, part3)
        return novo