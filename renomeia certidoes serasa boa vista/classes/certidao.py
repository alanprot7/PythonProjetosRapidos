class Certidao:

    def trazer_destino(self, dados):
        destino = 's'
        pesquisa = 'SERASA'
        achou = False
        for item in dados:
            if pesquisa in item:
                achou = True
        if not achou:
            destino = 'b'
        return destino 

    def trazer_data(self, dados):
        pos = 0
        pesquisa = 'NA DATA'
        for item in dados:
            if pesquisa in item:
                pos = item.find(pesquisa)
                data = item[pos:pos + 18].replace('/','')
                return data[-8:]

    def trazer_ato(self, dados):
        pesquisa = 'CANCELAMENTO'
        destino = 'c'
        achou = False
        for item in dados:
            if pesquisa in item:
                achou = True
        if not achou:
            destino = 'p'
        return destino