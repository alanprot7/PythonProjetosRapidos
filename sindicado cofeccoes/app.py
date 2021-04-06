from modulos import *
from classes.lista_cnpj import ListaCNPJ


def main():


    app = ListaCNPJ()

    dados = _arquivo.abrir('cnpjs.txt')
    cnpj_lista = app.listar_CNPJ(dados)

    cnpj_lista = list(set(cnpj_lista))

    print('Lista CNPJ com', len(cnpj_lista) )

    path_serasa = 'F:/Projetos/Serasa/2020'
    path_intimacoes = 'F:/Projetos/Notificacoes-STL/2020'
    path_filtro_renot = 'filtro_renot.txt'

    dir_serasa = _diretorio.listar_subdiretorios(path_serasa)
    dir_intimacoes = _diretorio.listar_subdiretorios(path_intimacoes)

    resultado_serasa = []

    pesquisa_serasa = app.gerar_pesquisa(cnpj_lista, 8)
    pesquisa_intima = app.gerar_pesquisa(cnpj_lista, 10)

    data_principal = 20200320

    cont = 0

    for serasa in dir_serasa:
        lista = _arquivo.abrir(serasa)
        dados = app.listar_dados_serasa(lista)
        for dado in dados:
            if dado[0] in pesquisa_serasa:
                if app.formatar_data(dado[2]) >= data_principal:
                    print('Protestado', dado[1], dado[2])
                    cont += 1
    print('Total:', cont)


    protocolos = []

    filiais = list()

    for intimacao in dir_intimacoes:
        lista = _arquivo.abrir(intimacao)
        dados = app.listar_dados_intimacoes(lista)
        for dado in dados:
            if dado[0] in pesquisa_intima:
                if app.formatar_data(dado[2]) >= data_principal:
                    protocolos.append('{}\t{}'.format(dado[1], dado[3]))
                    if '1-' not in dado[3]:
                        filiais.append(dado[3])

    filiais = sorted(list(set(filiais + cnpj_lista)))
    _arquivo.gravar('filiais.txt', filiais)

    protocolos = list(set(protocolos))
    protocolos = sorted(protocolos)

    _arquivo.gravar('renot_correios.txt', protocolos)

    print('Total Protocolos:', len(protocolos))

    prot_base = [prot[:7] for prot in protocolos]

    _arquivo.gravar('prot_base.txt', prot_base)

    renot = _arquivo.abrir(path_filtro_renot)

    renot_lista = app.separar_prot_filtrado(renot)

    pedidos = _arquivo.abrir('pedidos.txt')

    for item in pedidos:
        if item[:7] in renot_lista:
            print(item[:7], 'removido')
            renot_lista.remove(item[:7])

    _arquivo.gravar('perigo.txt', renot_lista)

    print('Total Perigo:', len(renot_lista))

    cont = 0

    resolvidos = []

    for item in protocolos:
        if item[:7] not in renot_lista:
            resolvidos.append(item)
            cont += 1

    _arquivo.gravar('resolvidos.txt', resolvidos)

    print('Total Resolvidos:', cont)

    input()

if __name__ == '__main__':
    main()