class Emolumento:


    def __init__(self, valores, custas):
        self.TAMANHO_ARRAY_CUSTAS = 10
        self.TAMANHO_ARRAY_VALORES = 6
        self.DIVISOR_BASE_100 = 100
        self.CODIGO_PAGO = '06'
        self.VALOR_PADRAO = 0.0
        self.valores = valores
        self.custas = custas
        self.cancelamento = []
        self.altera_tabela_decide_valor()


    def decide_valor(self, valor):

        posicao = self.TAMANHO_ARRAY_VALORES

        while not valor >= float(self.valores[posicao]):
            posicao -= 1

        custas = self.custas[posicao].split(';')
        return custas


    def decide_custas_cancelamento(self, valor):
        for item in self.custas:
            valor_base = float(item.split(';')[0]) / self.DIVISOR_BASE_100
            if valor == valor_base:
                return item.split(';')[1:]
  

    def verifica_protocolo(self, dado):
        start_codigo = 37
        end_codigo = 47
        if dado[0] == '7':
            start_codigo += 1
            end_codigo += 1
        protocolo  = dado[start_codigo:end_codigo]
        tamanho = len(str(int(protocolo)))
        if tamanho > 7:
            self.cancelamento.append(protocolo)
            return True


    def calcula_valores(self, arquivo):
        start_codigo = 108
        end_codigo = 110
        start_valor = 152
        end_valor = 165
        novo = []
        custas = []
        for item in arquivo:
            if item[start_codigo:end_codigo] == self.CODIGO_PAGO:
                valor_titulo = float(item[start_valor:end_valor]) / self.DIVISOR_BASE_100
                if self.verifica_protocolo(item):
                    custas = self.transforma_valor(self.decide_custas_cancelamento(valor_titulo))
                else:
                    custas = self.transforma_valor(self.decide_valor(valor_titulo))
                novo.append([custas, valor_titulo])
        valor_total = self.soma_valor(novo)
        valor_custas = self.soma_custas(novo)
        valor_total = valor_total - sum(self.transforma_valor(valor_custas))
        resultado = ';'.join(valor_custas) + ';{:.2f}'.format(valor_total)

        return self.gera_csv(resultado)


    def transforma_valor(self, lista):

        novo = [float(item) for item in lista]
        return novo


    def soma_custas(self, lista):

        novo = [self.VALOR_PADRAO] 
        novo = novo * self.TAMANHO_ARRAY_CUSTAS
        
        for item in lista:
            for index, valor in enumerate(item[0]):
                novo[index] += valor

        resultado = ['{:.2f}'.format(item) for item in novo]
        return resultado


    def soma_valor(self, lista):

        valor = self.VALOR_PADRAO

        for item in lista:
            valor += item[1]

        return valor


    def gera_csv(self, tabela):

        tabela_csv = ['EMOL;ISS;FAADEP;FRMMP;FERM;SELO;DISTRIBUIDOR;TARIFA;TARIFA CANCELAMENTOS;CORREIOS;VALOR REPASSE']
        tabela_csv.append(tabela.replace('.',','))

        return tabela_csv
    

    def altera_tabela_decide_valor(self):
 
        for index, valor in enumerate(self.valores):
            custas = self.transforma_valor(self.decide_valor(float(valor)))
            self.valores[index] = float(valor) + sum(custas)