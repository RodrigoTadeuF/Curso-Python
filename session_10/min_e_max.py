"""
Min e Max

max() -> retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))

print(max(4, 67, 54))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'g'))

print(max(3.14, 5.67))

print(max('Geek University'))

min() -> retorna o menor em um iteravel ou o menor de dois ou mais elementos

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))

print(min(4, 67, 54))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'g'))

print(min(3.14, 5.67))

print(min('Geek University'))

# Outros exemplos

nomes = ['Arya', 'Samsa', 'Tyron', 'John', 'Dany']

print(max(nomes))

print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))

print(min(nomes, key=lambda nome: len(nome)))
"""

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Hells Beels", "tocou": 32},
]

print(min(musicas, key=lambda musica: musica['tocou']))
print(max(musicas, key=lambda musica: musica['tocou']))

# DESAFIO!

print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])

# DESAFIO!

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])