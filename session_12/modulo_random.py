"""
Módulo Random e o que são módulos:

- Em Python módulos nada mais são do que arquivos Python.

Módulo random -> Possuí várias funções para geração de números pseudo-aleatórios.
"""
# OBS: existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - importando todo o módulo

import random

# Gera um número pseudo-aleatório entre 0 e 1

# OBS: Ao realizar o import do módulo completo todas as funções, atributos, classes e propriedades que
# tiverem dentro do módulo ficarão disponíveis (em memória). Se for o caso de conhecimento das funções
# que serão utilizadas devemos, então não é ideal que se faço o import do pacote completo.

print(random.random())

# veja que para utilizar a função random do pacote random colocamos o nome do pacote e o nome da função
# separados por ponto.

# Forma 2

from random import random

for i in range (10):
    print(random())

# uniform() -> Gerar um valor aleatório entre algum pré estabelecido

from random import uniform

for i in range (10):
    print(uniform(3, 7)) # 7 não é incluído

# randint() -> Gera valores pesudo aleatórios entre valores estabelecidos

from random import randint

for i in range(6):
    print(randint(1, 61), end=", ")

# choice() -> mostra um valor aleatório em um iteravel

from random import choice

jogadas = ["pedra", "papel", "tesoura"]

print(choice(jogadas))

# shuffle() -> função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']

print(cartas)
shuffle(cartas)
print(cartas)