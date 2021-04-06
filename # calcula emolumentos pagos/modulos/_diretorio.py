import os

def listar(path = os.getcwd()):
    lista = []
    for item in os.listdir(path):
        rota = os.path.join(path, item)
        lista.append(rota)
    return lista

def listar_subdiretorios(path = os.getcwd()):
    lista = []
    for root, dirs, files in os.walk(path):
        for file in files:
            rota = os.path.join(root, file)
            lista.append(rota)
    return lista