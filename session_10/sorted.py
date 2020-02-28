"""
Sorted

OBS: Não confundir com sort()
O sort() funciona apenas em listas.

O sorted() pode ser utilizado em qualquer iterável.

Como o próprio nome diz, sorted serve para ordenar elementos

O sorted(), SEMPRE retorna uma Lista com os elementos do iterável ordenados

# Exemplo

numeros = [ 6, 1, 8, 2]
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)

# Adicionando parâmetros ao sorted()

numeros = [ 6, 1, 8, 2]

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor


# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "dogge", "tweets": ["Eu amo cachorros", "Hoje tem festa"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"},
]

print(usuarios)

print(sorted(usuarios, key=lambda user: user["username"]))
"""
# Último exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Hells Beels", "tocou": 32},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da menos tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))