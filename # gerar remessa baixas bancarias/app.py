from modulos import *
from classes.remessa_itau import RemessaItau
from classes.remessa_bb import RemessaBB


def listar_conteudo_arquivos(path):
    lista_conteudo = []
    diretorio = _diretorio.listar_subdiretorios(path)
    for nome in diretorio:
        if '.txt'.upper() in nome.upper():
            arquivo = _arquivo.abrir(nome)
            lista_conteudo += arquivo
    return lista_conteudo
    

def main():

    app_itau = RemessaItau()
    app_bb = RemessaBB()
    path_protocolos = 'F:/Projetos/COBRANCA-ITAU/2021'
    path_sinc = 'arquivos/arquivo_sinc'
    path_remessa = 'arquivos/remessa_bb'
    path_protocolos_bb = 'F:/Projetos/COBRANCA-BB'

    protocolos = app_itau.montar_base_pesquisa(listar_conteudo_arquivos(path_protocolos))
    arq_sinc = app_itau.catalogar_protocolos_sinc(listar_conteudo_arquivos(path_sinc))
    remessa_bb = app_itau.catalogar_protocolos_remessa(listar_conteudo_arquivos(path_remessa))
    
    remessa_itau = app_itau.montar_arquivo(arq_sinc + remessa_bb , protocolos)
    nome_saida = 'CC{}32.txt'.format(app_itau.data[:4])
    _arquivo.gravar('arquivos/saida_itau/' + nome_saida, remessa_itau)

    protocolos = app_bb.catalogar_protocolos_remessa(listar_conteudo_arquivos(path_protocolos_bb))
    linhas_bb = app_bb.catalogar_linhas_remessa(listar_conteudo_arquivos(path_protocolos_bb))
    remessa_bb_saida = app_bb.montar_arquivo_bb(arq_sinc, linhas_bb , protocolos)

    _arquivo.gravar('arquivos/saida_bb/' + 'C' + nome_saida, remessa_bb_saida)    

if __name__ == '__main__':
    main()