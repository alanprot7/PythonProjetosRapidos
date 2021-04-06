class Baixas:
    
    def pega_protocolo_remessa(self, lista):
        protocolo = slice(73,80)
        novo = [item[protocolo] for item in lista if item[0] == '7']
        return novo

    def pega_protocolo_baixa(self, lista):
        protocolo = slice(23,30)
        chave = '0003253391000'
        novo = [item[protocolo] for item in lista if chave in item]
        return novo

    def gera_lista_renotificar(self, baixa, remessa):
        novo = [item for item in remessa if item in baixa]
        return novo

    def diferenca(self, maior, menor):
        novo = [item for item in maior if item not in menor]
        return novo