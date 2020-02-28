"""
Generators

Em aulas anteriores estudamos comprehension, porém não foi visto tuple comprehension
Por que elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))


# Poderiamos ter feito usando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Com Generator + performático
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

# Qual é a utilizade de getsizeof()? -> Retorna a quantidade em bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' ocupa em memória.
print(getsizeof('Geek'))

"""

# Como iterar no Generator Expression

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)