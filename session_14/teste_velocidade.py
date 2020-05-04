"""
Teste de Velocidade com expressões Geradoras


# Generators são os geradores

def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()
print(ge1)  # Generator

print(next(ge1))
print(next(ge1))

# Generator Expression

ge2 = (num for num in range (1, 10))

print(ge2)

print(next(ge2))
print(next(ge2))

"""
# Realizando o teste de velocidade
import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(1, 100000000)))
gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio

print(f'Generation Expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')
