import os

lista = []

with open('unicos.txt') as entrada:
    lista = entrada.read().splitlines()

def get_key(item):
    return item[:7]

lista = [x[:20] for x in lista]

lista_set = set(lista)

lista = sorted(list(lista_set), key=get_key)


criticos = os.listdir('P:/IMG_CRITICOS')

criticos = [x[-11:-4] for x in criticos]

novo = [x for x in lista if x[:7] not in criticos]

[print(x) for x in novo]

print(len(novo))