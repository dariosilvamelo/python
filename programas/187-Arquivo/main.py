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

import os

menu = ''

caminho_arquivo = '.\\187-Arquivo\\arquivo_inicial.txt'
novo_caminho = '.\\187-Arquivo\\arquivo_novo.txt'

with open(caminho_arquivo, 'x', encoding='utf8') as arquivo:
    ...
arquivo2 = arquivo


def escrever(arquivo):
    # W OU W+ = APAGA O CONTEUDO DO ARQUIVO E FICA ABILITADO PARA ESCREVER
    with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:
        # encoding='utf8' -> serve para formatar os caracteres especiais
        arquivo.write('Atenção\n')
        arquivo.write('Linha 1\n')
        arquivo.write('Linha 2\n')
        arquivo.writelines(
            ('Linha 3\n',
             'Linha 4\n'))  # escrever varias linhas
        arquivo.seek(0, 0)
        print(arquivo.read(), end='')
        print('Também estou lendo!')


def adicionar(arquivo):
    # a OU a+ = não apaga o conteudo do arquivo, vair para o final do arquivo e pode acrescentar dados no final do arquivo
    with open(caminho_arquivo, 'a+', encoding='utf8') as arquivo:
        arquivo.write('Linha ....\n')
        arquivo.write('Linha ....\n')
        # encoding='utf8' -> serve para formatar os caracteres especiais
        arquivo.write('Linha ....\n')
        arquivo.seek(0, 0)
        print(arquivo.read())
        print('Também estou lendo!')


def criar(arquivo2):
    with open(novo_caminho, 'x', encoding='utf8') as arquivo:
        ...


def ler(arquivo):
    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
        print(arquivo.read())
        arquivo.seek(0, 0)
        arquivo.readline()  # É COMO SE FOSSE O NEXT: LE A LINHA E PASSA PARA A PROXIMA LINHA
        arquivo.readline()
        print(arquivo.readline(), end='')
        # strip eliminas espaços em barnco e quebra de linha do inicio e no final da linha
        print(arquivo.readline().strip())


def ler_linhas(inicio, fim, arquivo):
    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
        arquivo.seek(0, 0)
        contador = 0
        for linha in arquivo.readlines():
            if contador >= inicio and contador <= fim:
                print(linha.strip())
            contador += 1


while menu != 'S':
    menu = input(
        '[C]riar, [E]screve, [A]dicionar, [L]er, Ler L[I]nha, [R]enomear, [D]eletar, [S]air:')
    if menu == 'C':
        criar(arquivo2)
    elif menu == 'E':
        escrever(arquivo)
    elif menu == 'A':
        adicionar(arquivo)
    elif menu == 'L':
        ler(arquivo)
    elif menu == 'I':
        inicio = int(input('Entre com o inicio da linha:'))
        fim = int(input('Entre com o fim da linha:'))
        ler_linhas(inicio, fim, arquivo)
    elif menu == 'R':
        # renomea e pode mudar de local caso queira, no local de origem o arquivo não vai exeistir mais
        os.rename(caminho_arquivo,
                  'D:\\Informatica\\Python\\programas\\187-Arquivo\\arquivo\\Arquivo_Renomeado.txt')
    elif menu == 'D':
        # remover arquivo: remove ou unlink
        os.remove(novo_caminho)
        os.unlink(
            'D:\\Informatica\\Python\\programas\\187-Arquivo\\arquivo\\Arquivo_Renomeado.txt')
        ...
print('Fim!')
