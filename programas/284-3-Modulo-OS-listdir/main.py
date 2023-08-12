# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
import os

# caminho = 'D:\\Informatica\\Python\\programas\\190-JSON'
caminho = 'D:\\Informatica\\Python\\programas'

diretorios = caminho.split('\\')
print(diretorios)
# ou

# caminho = os.path.join('/Informatica', 'Python', 'programas', '190-JSON')
print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    # vai checar se a pasta é um diretorio
    if not os.path.isdir(caminho_completo_pasta):
        continue

    for i in os.listdir(caminho_completo_pasta):
        print('  ', i)
