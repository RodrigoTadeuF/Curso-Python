"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou se ainda  iterável está vazio

# Exemplo all

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False (0)
print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True
print(all([]))  # Todos os números são verdadeiros? True

nomes = ['Carlos', 'Camila', 'carla', 'Cassiano', 'Cristina']

print(all(nome[0] == 'C' or 'c' for nome in nomes))

print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

any() -> Retorno True se qualquer elemento do iteravel for verdadeiro. Se o iterável estiver vazio, retorna False.
"""

print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, {}, {}, []]))  # False

nomes = ['Carlos', 'Camila', 'carla', 'Cassiano', 'Cristina']

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))
