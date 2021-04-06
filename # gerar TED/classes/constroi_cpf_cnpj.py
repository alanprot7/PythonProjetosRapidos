from valida_cpf_cnpj import *

def create_CPF(num):
    count = 0
    while True:
        digit = '{:02d}'.format(count)
        new_CPF = f'{num}{digit}'
        if isCPF(new_CPF):
            print(new_CPF)
            break
        else:
            count += 1

def create_CNPJ(num):
    count = 0
    while True:
        digit = '{:02d}'.format(count)
        new_CNPJ = f'{num}{digit}'
        if isCNPJ(new_CNPJ):
            print(new_CNPJ)
            break
        else:
            count += 1

num = input('Documento: ')

if len(num) < 10:
    create_CPF(num)
else:
    create_CNPJ(num)

input()