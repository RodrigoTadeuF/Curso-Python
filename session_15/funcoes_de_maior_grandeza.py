"""
Funções de Maior Grandeza - Higher Order Functions = HOF

O que isso significa?

- Quando uma linguagem de programação suporta HOF indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
nos nossos programas.

OBS: Na sessão de funções, já foi utilizado isso.

Em Python as funções são Cidadões de primeira Classe, First Class Citizens


# Exemplo - Definindo as funções

def somar(a, b):
    return a + b


def subratir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções

print(calcular(4, 3, somar))

print(calcular(4, 3, subratir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))

"""

"""
# Nested Functions - Funções aninhadas

Em Python podemos ter funções dentro de funções, que são conhecidas por Nested Functions
ou também Inner Functions (Funções Internas).


# Exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

# Testando
print(cumprimento('Rodrigo'))

print(cumprimento('Tadeu'))
"""

# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahah', 'kkkkkkkkkkkkkk', 'haeuheauheauheuheau'))
    return rir

rindo = faz_me_rir()
print(rindo())

# Inner functions ou Nested functions podem acessar o escopo de funções externas

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahaha', 'kkkkkk', 'haeuhaeuh'))
        return f'{risada} {pessoa}'
    return dando_risada

# Testando

rindo = faz_me_rir_novamente('Rodrigo')

print(rindo())
print(rindo())
print(rindo())
