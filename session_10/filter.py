"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados usando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda valor: valor > media, dados)
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))


paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(lambda pais: len(pais) > 0, paises)
res = filter(lambda pais: len(pais) != '', paises)
print(list(res))

# A diferença entre Map e Filter é:

# map() -> recebe dois parâmetros, uma função e um iteravel e retorna um objeto mapeando a função para cada elemento do
# iteravel

# filter() -> recebe dois parâmetros, uma função e um iteravel e retorna um objeto filtrando apenas os elementos de
# acordo com a função.

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "dogge", "tweets": ["Eu amo cachorros", "Hoje tem festa"]},
    {"username": "gal", "tweets": []},
]

print(usuarios)

# Filtrar os usuários que estão inativos no Twitter

# Forma 1
# inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda user: not user['tweets'], usuarios))

print(inativos)
"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo:
# 'Sua instrutora é' + nome, desde que cada nome tenha menos de cinco caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)