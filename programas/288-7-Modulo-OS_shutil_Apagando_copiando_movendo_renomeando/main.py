# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
import os
import shutil

PASTA_ORIGINAL = os.path.join(
    'D:\\Informatica\\Python', 'Copia_Seguraca_programa')

NOVA_PASTA = os.path.join(
    'D:\\Informatica\\Python', 'Copia_Seguraca_programa_02')

# Apaga diretorios, sub diretorios e arquivos recursivamente
shutil.rmtree(NOVA_PASTA, ignore_errors=True)

# Copia diretorios, sub diretorios e arquivos recursivamente
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

# Renomeia e move
shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')
