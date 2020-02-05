"""
Loop for

Loop -> Estrutura de Repetição.
For -> Uma dessas estruturas

C ou Java

for (int i = 0; i < limitador; i++) {
    // execução do loop
}

Python

for item in interavel:
    // execução do loop



Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis

Exemplos de iteráveis:
 - String
   nome = 'Geek University'
 - Lista
   lista = [1, 3, 5, 7, 9]
 - Range
   numeros = (1, 10)


# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando em uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando em um range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive

for numero in range(1, 10):
    print(numero)

Enumarate:

((0, 'G'),(1, 'e')...)

for i, letra in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não usamos um valor podemos descartá-lo com um (_) underline

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = (1, 10)  # temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor'))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')
"""

# Original: U+1F60D
# Modificado: U0001F60D

for x in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)
