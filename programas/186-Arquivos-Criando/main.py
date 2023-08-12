# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = '.\\186-Arquivos-Criando\\novo_aquivo.txt'
'''
arquivo = open(caminho_arquivo, 'w')
print('Olá mundo')
print('Arquivo vai ser fechado') 
arquivo.close()
ou
'''
with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')

print(type(arquivo))
print(bool(arquivo))

'''
ou
se fizer com a opção " x ", caso o aquivo exista
e pedir para criar novamente vai dar erro
se usarmos a opção " w ", e o arquivo já exitir
não vai dar erro mas vai apagar tudo que estiver no arquivo.

with open(caminho_arquivo, 'x') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')

'''
