
import shutil
from pathlib import Path

caminho_projeto = Path()
print(caminho_projeto.absolute())

print('Exercicio 01:')
caminho_projeto = Path(__file__)
print(caminho_projeto)
print(caminho_projeto.parent)
print(caminho_projeto.parent.parent)
print(caminho_projeto.parent.parent.parent)
print(caminho_projeto.parent.parent.parent.parent)
print(caminho_projeto.parent.parent.parent.parent.parent)
print('==================================')

print('Exercicio 02')
# para salvar um arquivo na area de trabalho
caminho_arquivo = Path.home() / 'Desktop' / 'Python'
caminho_arquivo.mkdir(exist_ok=True)  # criou a pasta fisicamente

caminho_arquivo = caminho_arquivo / 'Execicio_292'
caminho_arquivo.mkdir(exist_ok=True)  # criou outra sub pasta fisicamente

caminho_arquivo = caminho_arquivo / 'arquivo.txt'
caminho_arquivo.touch()  # criou o arquivo fisicamente

# sempre vai salvar apenas a ultima inserção de escrita.
caminho_arquivo.write_text('linha1: Ola Mundo!')
caminho_arquivo.write_text('linha2: dinovo Ola Mundo!')
caminho_arquivo.write_text('linha3: dinovo Ola Mundo!')

s = caminho_arquivo.read_text()  # sempre vai pegar a ultima
print(s)
print('==================================')

apaga = Path.home() / 'Desktop' / 'Python'

# shutil.rmtree(apaga, ignore_errors=True)  # apaga tudo
# print('Caminho apagado!')
'''
caminho_arquivo.unlink()  # apaga o arquivo, somente o aruivo
print(caminho_arquivo)
'''
