import xmltodict
import os

def abrir(path):
    with open(path, encoding='utf-8') as entrada:
        dados = entrada.read()
        return dados


def converte(valor):
    novo = float(valor.replace('.','').replace(',','.'))
    return novo


def valor_str(valor):
    novo = '{:.2f}'.format(valor)
    return novo


path = ''.join([x for x in os.listdir() if '.xml' in x])

doc = xmltodict.parse(abrir(path))
caixa = doc['cartorio']['caixa']['transacoes']['transacao']
valor_geral = 0.0

for sequencial in caixa:

    chaves = ['emolumento','fermoju','selo','iss','faadep','frmmp']
    taxa_ar = 0.0
    valor_ref = converte(sequencial['valor'])
    tipo = sequencial['tipo']
    valor_total = 0.0


    if 'titulo' in sequencial['Titulos']:
        atos = sequencial['Titulos']['titulo']
    elif 'certidao' in sequencial['certidao']:
        atos = sequencial['certidao']['certidao']
    else:
        atos = []
        valor_total = valor_ref
    
    
    if type(atos) == list:
        for ato in atos:
            for custas in ato['Atos']['ato']:
                for chave in custas:
                    if chave in chaves:
                        valor_total += converte(custas[chave])
            if 'ValorAR' in ato:
                taxa_ar += converte(ato['ValorAR'])
    
    elif tipo == 'Certidao':
        custas = atos['Atos']['ato']
        for chave in custas:
            if type(chave) == str:
                if chave in chaves:
                    valor_total += converte(custas[chave])
            else:
                for codigo in chave:
                    if valor_ref <= 40.09:
                        if codigo in chaves:
                            valor_total += converte(chave[codigo])
                    else:
                        if codigo == 'atos':
                            for adicional in chave[codigo]:
                                for novo in chave[codigo][adicional]:
                                    if type(novo) != str:
                                        for cod_novo in novo:
                                            if cod_novo in chaves:
                                                valor_total += converte(novo[cod_novo])
    else:
        for custas in atos['Atos']['ato']:
            for chave in custas:
                if chave in chaves:
                    valor_total += converte(custas[chave])
        if 'ValorAR' in atos:
            taxa_ar += converte(atos['ValorAR'])

    valor_total += taxa_ar

    

    if valor_str(valor_ref) != valor_str(valor_total):
        print('id', sequencial['codigo'], 'Valor Pago: ',valor_str(valor_ref),'Valor Calculado:',valor_str(valor_total), 'Dif', valor_str(valor_total - valor_ref))
        valor_geral += valor_total

print('Total Caixa:', '{:.2f}'.format(valor_geral))