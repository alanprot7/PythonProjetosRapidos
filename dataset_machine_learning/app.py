from modulos import *

def load_all(path):
    conteudo = []
    arquivos = _diretorio.listar_subdiretorios(path)
    for arquivo in arquivos:
        if '.txt' in arquivo:
            conteudo += _arquivo.abrir(arquivo)
    return conteudo

def cria_pagos(lista):
    novo = [item[:7] for item in lista if item[:2] == '15']
    return novo

def cria_csv(intimacoes, pagos_protocolos):
    csv = set()
    for item in intimacoes:
        if item[:2] == '07':
            protocolo = item[191:198]
            especie = item[208:211].strip()
            valor = float(item[289:299]) / 100
            cep_raiz = item[424:429].strip()
            status_pago = 0
            if protocolo in pagos_protocolos:
                status_pago = 1
            if cep_raiz:
                if cep_raiz != '60000':
                    csv.add(f'{protocolo},{especie},{cep_raiz},{valor},{status_pago}')
    csv = list(csv)
    csv.insert(0, 'protocolo,especie,cep_raiz,valor,status_pago')

    return csv

def cria_tipo(item):
    tipo = 'CNPJ'
    if len(item[52:70].strip()) < 18:
        tipo = 'CPF'
    return tipo

def main(): 

    path_intimacoes = 'F:/Projetos/Notificacoes-STL/2020'
    intimacoes = load_all(path_intimacoes)
    pagos = _arquivo.abrir('pagos.txt')
    pagos_protocolos = cria_pagos(pagos)
    csv = cria_csv(intimacoes, pagos_protocolos)
    _arquivo.gravar('quitacoes_por_localidade.csv', csv)
    

if __name__ == '__main__':
    main()