# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

# HOME = os.path.expanduser('~')
# DESKTOP = os.path.join(HOME, 'Desktop')

PASTA_ORIGINAL = 'D:\\Informatica\\Python\\programas'
NOVA_PASTA = os.path.join(
    'D:\\Informatica\\Python', 'Copia_Seguraca_programa')


os.makedirs(NOVA_PASTA, exist_ok=True)  # Cria uma pasta caso ela não exista

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        # replace troca o valor de uma string por outroa
        caminnho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        # cria diretorio caso não exista.
        os.makedirs(caminnho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminnho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        # faz a copia do arquivo
        shutil.copy(caminho_arquivo, caminnho_novo_arquivo)
        print(caminnho_novo_arquivo)
print('')
print('Fim da Copia de Segurança!')
