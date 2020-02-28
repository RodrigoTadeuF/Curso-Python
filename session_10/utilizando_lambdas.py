"""
Utilizando Lambdas

Conhecidas como Expressões Lambdas ou simplesmente Lambdas, são funcções sem nome, ou seja,
funções anônimas.

# Função em Python


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressão Lambda
lambda x: 3 * x + 1

# E como utilizar a expressão Lambda
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com múltiplas entradas
# Strip = Trim(Java)

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' rodrigo', 'TADEU'))
print(nome_completo(' rodrigo                  ', 'TaDeU'))

# Em funções Python podemos ter nenhuma ou várias entradas, em Lambdas também

expressao = lambda: 'We <3 Python!'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y ) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, ... xn: uma expressão

print(expressao())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

#OBS: se for passado mais ou menos parametros ou argumentos teremos um erro!

# Outro exemplo

autores = [' Isaac Asimov', 'Machado de Assis', 'Artur C. Clarke', 'William Shakespeare', 'Frank Hebert',
           'Graciliano Ramos', 'Annie Frank']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
"""


# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_funcao_quadratica(a, b, c):
    """ Retorna a função f(x) a*x**2 + b*x + c """
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))
