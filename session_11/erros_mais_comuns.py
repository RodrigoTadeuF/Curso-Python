"""
Erros mais comuns em Python

ATENÇÃO: É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso Código.

Erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que
o Python não reconhece como parte da linguagem.

# Exemplo SyntaxError

def funcao:
    print('Geek University')

NameError -> Ocorre quando uma variável ou uma função não foi definida.

# Exemplo NameError

print(geek)

TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

# Exemplo TypeError

print(len(5))

IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido.

# Exemplo IndexError

lista = ['Geek']
print(lista[1])

ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto,
mas valor inapropriedado

# Exemplo ValueError

print(int('Geek'))

KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe

# Exemplo KeyError

dic = {}
print(dic['geek'])

AttributeError -> Ocorre quando uma variável não tem um atributo/função

# Exemplo AtrributeError

tupla = (11, 2, 31, 4)
print(tupla.sort())

IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

# Exemplo IndentationError

def nova():
print('Geek')

OBS: Exceptions e Erros são sinônimos na progração

OBS: Importante ler a documentação dos Erros.
"""

