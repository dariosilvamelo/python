"""
DocString
=========

isso não é um comentario

skdaskdçlsa
sadas
"""
'''
\r\n => CRLF
usado para escrever suas notas
'''
#comentário

print("Dário da \"Silva\" Melo")
print(r"Dário da \"Silva\" Melo")
print('Dário da "Silva" Melo')
print("Dário da 'Silva' Melo")
print(1234,'Dário da "Silva" Melo')
print(1 + 1)

print(        )
print(        )
print(        )

print(333, 33, sep="<>")
print(123, 34, sep='=', end='##')
print(456, 10, sep="<>", end='\n')
print(456, 10, sep="<>", end='\n')

print(0,1, -15, 15.35, 0.0, -20.01)
print(type(0),type(1),type(-15), type(15.35), type(0.0), type(-20.01))

print(        )
print(        )
print(        )

print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))

print(1 + 1)
print('a' +'b')
# print('1' + 4) -> da erro
print('===========')

print(int('1') + 4)
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b')
print('===========')
print('===========')

# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

nome_completo = 'Luiz Otávio Miranda'
soma_dois_mais_dois = 2 + 2
int_um = bool('1')
print(int_um, type(int_um))
print(nome_completo, soma_dois_mais_dois)

nome = 'Luiz'
idade = 17
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)

