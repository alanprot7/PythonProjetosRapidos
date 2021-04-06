class Emolumentos:

    def __init__(self):
        self.valor_total = 0.0

    def somar_emolumentos(self, dados):
        for item in dados:
            if 'TOTAL' in item:
                total_arr = item.split(' ')
                if len(total_arr) > 6:
                    if total_arr[0] == 'TOTAL': 
                        valor = float(total_arr[2].replace('.', '').replace(',', '.'))
                        self.valor_total += valor
