class Comparador:

    def comparar_caracteres(self, dados1, dados2):
        linha1 = dados1[519:554]
        linha2 = dados2[519:554]
        diferenca = ''
        for index, item in enumerate(linha1):
            if item != linha2[index]:
                diferenca += 'pos:{} '.format(index + 1)                

        if diferenca:        
            print('Diferenças: {}'.format(diferenca))
            print(linha1)
            print(linha2)

