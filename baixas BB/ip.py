from modulos import *

path = '1533556.pdf'

ip = _pdf.ler(path)

for index, item in enumerate(ip):
    if 'Valor Protestado' in item:
        array = ip[index + 1].split(' ')
        print(array[-1])
