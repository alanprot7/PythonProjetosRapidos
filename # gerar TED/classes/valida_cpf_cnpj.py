def cria_invalidos(tamanho):
    lista = []
    for item in range(10):
        numeros = str(item) * tamanho
        lista.append(numeros)
    return lista

def isCPF(doc):
    invalidos = cria_invalidos(11)

    if len(doc) != 11 or doc in invalidos:
        return False

    try:
        sm = 0
        peso = 10
        dig10 = dig11 = num =0

        for item in range(9):
            num = (int)(doc[item])
            sm = sm + (num * peso)
            peso = peso - 1

        r = 11 - (sm % 11)
        if r == 10 or r == 11:
            dig10 = '0'
        else:
            dig10 = str(r)


        sm = 0
        peso = 11
        for item in range(10):
            num = (int)(doc[item])
            sm = sm + (num * peso)
            peso = peso - 1


        r = 11 - (sm % 11)
        if r == 10 or r == 11:
            dig11 = '0'
        else:
            dig11 = str(r)

        if dig10 == doc[9] and dig11 == doc[10]:
            return True
        else:
            return False
    except:
        return False

def isCNPJ(doc):
    invalidos = cria_invalidos(14)

    if len(doc) != 14 or doc in invalidos:
        return False

    try:
        sm = 0
        peso = 2
        dig13 = dig14 = num =0

        for item in range(11,-1,-1):
            num = (int)(doc[item])
            sm = sm + (num * peso)
            peso = peso + 1
            if peso == 10:
                peso = 2

        r = sm % 11
        if r == 0 or r == 1:
            dig13 = '0'
        else:
            dig13 = str(11 - r)


        sm = 0
        peso = 2
        for item in range(12,-1,-1):
            num = (int)(doc[item])
            sm = sm + (num * peso)
            peso = peso + 1
            if peso == 10:
                peso = 2

        r = sm % 11
        if r == 0 or r == 1:
            dig14 = '0'
        else:
            dig14 = str(11 - r)


        if dig13 == doc[12] and dig14 == doc[13]:
            return True
        else:
            return False
    except:
        return False

