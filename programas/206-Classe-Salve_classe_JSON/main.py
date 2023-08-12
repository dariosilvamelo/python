import json

CAMINHO_ARQUIVO = '.\\206-Classe-Salve_classe_JSON\\arquivo_pessoa.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)

# Posso usar tanto vars quanto __dict__ estou apenas exemplificado
bd = [vars(p1), p2.__dict__, vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)


# como o outro arquivo "recebendo_dados_JSON.py"
# importa esse arquivo "main.py"
# quando o arquivo "recebendo_dados_JSON.py" for executado ele
# chamara a função "fazer_dump"
# para evitar isso podemos fazer a logica abaixo:
# quando o arquivo "recebendo_dados_JSON.py" está sendo executado ele passa
# a ser o main e o aquivo "main.py" deixa de ser main
if __name__ == '__main__':
    fazer_dump()
