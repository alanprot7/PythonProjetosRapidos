class ListaCNPJ:

    
    def listar_CNPJ(self, dados):
        cnpj_lista = []
        for item in dados:
            pos = item.find('/00')
            if pos > -1:
                cnpj = '{}'.format(item[pos-10:pos+9]).strip()
                cnpj = cnpj.replace(' ','')
                if len(cnpj) > 10:
                    cnpj_lista.append(cnpj)
        return cnpj_lista          

    
    def listar_dados_serasa(self, arquivo):
        novo = []
        for item in arquivo:
            if '1P' in item[:2]:
                cnpj = item[346:354]
                protocolo = item[450:457]
                data = item[260:268]
                novo.append([cnpj, protocolo, data])
        return novo

    
    def listar_dados_intimacoes(self, arquivo):
        novo = []
        for item in arquivo:
            if '07' in item[:2]:
                cnpj = item[52:62]
                cnpj_completo = item[52:70]
                protocolo = item[191:198]
                data = item[299:309]
                novo.append([cnpj, protocolo, data, cnpj_completo])
        return novo

    
    def formatar_data(self, data):
        novo = data.replace('/', '').strip()
        dia, mes, ano = novo[:2], novo[2:4], novo[4:]
        return int(ano + mes + dia)

    
    def gerar_pesquisa(self, dados, tamanho):
        pesquisa = set()
        for item in dados:
            if tamanho == 8:
                item = item.replace('.', '').strip()
            pesquisa.add(item[:tamanho])
        return pesquisa

    def separar_prot_filtrado(self, dados):
        novo = []
        for item in dados:
            if 'Protocolo' in item:
                if len(item) > 60:
                    novo.append(item[11:18])
        return novo