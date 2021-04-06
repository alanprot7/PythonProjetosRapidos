from modulos import *
from datetime import datetime

def obter_lista(path):
    lista = []
    for item in _diretorio.listar_subdiretorios(path):
        lista.append(item)
    diretorio = lista[0].split('\\')[-2]
    return [diretorio, lista]

def listar_codigos(arquivos):
    lista = []
    for nome in arquivos:
        arquivo = _pdf.ler(nome)
        lista += extrair_codigo(arquivo)
    return lista

def extrair_codigo(arquivo):
    lista = set()
    for item in arquivo:
        item_split = item.split(' ')
        if item[0] == '8' and len(item_split) == 4:
            codigo = ''.join([x[:11] for x in item_split])
            lista.add(codigo)
    return list(lista)

def gerar_instrucao(diretorio, codigos):
    now = datetime.now()
    data = now.strftime('%d%m%Y')
    lista = []
    sigla = 'SEGO'
    beneficiario = diretorio
    for item in codigos:
        codigo = item
        valor = int(item[4:15])
        vencimento = ajustar_data(item[19:27])
        lista.append(f'{sigla};{codigo};{beneficiario};{vencimento};{data};{valor}')
    return lista


def ajustar_data(data):
    dia = data[-2:]
    mes = data[-4:-2]
    ano = data[:4]
    return f'{dia}{mes}{ano}'

path = 'boletos'

diretorio, lista = obter_lista(path)

codigos = listar_codigos(lista)

resultado = gerar_instrucao(diretorio, codigos)

_arquivo.gravar('codboletos.txt', resultado)