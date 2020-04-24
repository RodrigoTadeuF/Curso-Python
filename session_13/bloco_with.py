"""
O bloco with

passos para se trabalhar com arquivos
# 1 - abrimos o arquivo
# 2 - manipulamos o arquivo
# 3 - fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalho, onde os recursos utilizados são
fechados após o bloco with.

"""

# O bloco with

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
