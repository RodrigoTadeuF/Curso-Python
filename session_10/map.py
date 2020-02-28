"""
Map

Com 'Map' fazemos mapeamentos de valores para função.


import math

def area(r):
      # Calcula a área de um círculo com raio 'r'
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - Usando Map

# Map é uma função que recebe dois parâmetros: o primeiro uma função, o segundo um iterável

areas = map(area, raios)
print(type(areas))
print(list(areas))

# Forma 3 - Map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

#OBS: após utilizar a função map, depois da primeira utilziação do resultado ele é zerado

# Para fixar - MAP

# Temos dados iteraveis

# Temos uma função

# Utilizamos uma função map(f, dados) onde o map irá 'mapear' cada elemento dos dados e aplicar a função.

# O mapObject após ser utilizado será descartado
"""

# Mais exemplos

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

print(cidades)

# F = 9/5 * C + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))
