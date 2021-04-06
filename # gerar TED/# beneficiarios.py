import os
from classes.valida_cpf_cnpj import *

path = 'config/beneficiarios.txt'

def limpa_pontuacao(documento):
    documento = documento.replace('.','').replace('-','').replace('/','')
    return documento

def formata_cpf(documento):
    documento = limpa_pontuacao(documento)
    part1 = documento[:3]
    part2 = documento[3:6]
    part3 = documento[6:9]
    part4 = documento[9:]
    return f'{part1}.{part2}.{part3}-{part4}'


def formata_cnpj(documento):
    documento = limpa_pontuacao(documento)
    part1 = documento[:2]
    part2 = documento[2:5]
    part3 = documento[5:8]
    part4 = documento[8:12]
    part5 = documento[12:]
    return f'{part1}.{part2}.{part3}/{part4}-{part5}'


def deletar(posicao, beneficiarios):
    opcao = input('Deseja deletar? (s/n): ').lower()
    if opcao == 's':
        del beneficiarios[posicao]
        gravar(path, beneficiarios)
        print('Deletado com Sucesso!')        


def consulta_cadastro(codigo, beneficiarios):
    os.system('cls')
    codigos = [x.split(';')[0] for x in beneficiarios]
    posicao = codigos.index(codigo)
    dados = beneficiarios[posicao].split(';')
    print(f'Código: {dados[0]}')
    print(f'Banco: {dados[1]}')
    print(f'Agencia: {dados[2]}-{dados[3]}')
    print(f'Conta: {dados[4]}-{dados[5]}')
    print(f'Nome: {dados[6]}')
    print(f'Tipo: {dados[7]}')
    if dados[7] == '1':
        documento = formata_cpf(dados[8])
    else:
        documento = formata_cnpj(dados[8])
    print(f'CPF/CNPJ: {documento}\n')
    deletar(posicao, beneficiarios)

def gravar(path, lista):
    with open(path, 'w') as saida:
        for item in lista:
            saida.write(f'{item}\n')


def abrir(path):
    with open(path) as entrada:
        dados = entrada.read().splitlines()
        return dados


def checa_cadastro(codigo, beneficiarios):
    codigos = [x.split(';')[0] for x in beneficiarios]
    if codigo in codigos:
        return True


def cadastra_novo(beneficiarios):
    codigo = input('Informe o Código: ').upper()
    if checa_cadastro(codigo, beneficiarios):
        print('\nBeneficiário já Cadastrado!')
        opcao = input('\nMostrar cadastro? (s/n): ').lower()
        if opcao == 's':
            consulta_cadastro(codigo, beneficiarios)
        return False
    tipo_pessoa = input('Tipo de Pessoa Fisica(1)/Juridica(2): ')
    documento = limpa_pontuacao(input('Informe o CPF/CNPJ: '))
    if tipo_pessoa == '1':
        if not isCPF(documento):
            print('CPF Incorreto!')
            return False
    elif tipo_pessoa == '2':
        if not isCNPJ(documento):
            print('CNPJ Incorreto!')
            return False
    else:
        print('Tipo de pessoa Incorreto!')
        return False
    nome = input('Informe Nome: ').upper()
    banco = input('Codigo do Banco: ')
    agencia = input('Agencia: ')
    digito_agencia = input('Dígito: ')
    conta = input('Conta: ')
    digito_conta = input('Dígito: ')

    return f'{codigo};{banco};{agencia};{digito_agencia};{conta};{digito_conta};{nome};{tipo_pessoa};{documento}'


while True:
    beneficiarios = abrir(path)
    novo = cadastra_novo(beneficiarios)
    if novo:
        beneficiarios.append(novo)
        gravar(path, beneficiarios)
        print('\nCadastrado Com Sucesso!')        
    input()
    os.system('cls')