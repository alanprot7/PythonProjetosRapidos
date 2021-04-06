from modulos import _pdf
import os
import shutil

path = 'P:/'
path_destino = 'F:/Projetos/Certidões Assinadas Digitalmente'
count = 0

for item in os.listdir(path):
    origem = os.path.join(path, item)
    destino = None
    # if '.pdf'.upper() in item.upper():
    #     pdf = ''.join(_pdf.ler(origem))
    if 'CERTID' in origem.upper():
        destino = os.path.join(path_destino, item)
    if destino:
        if not os.path.exists(destino):
            shutil.move(origem, destino)        
            print('Movido', destino)
            count += 1

print(count) 
input()