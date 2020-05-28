"""
Lendo Arquivos CSV

CSV - Comma Separated Values - Valores Separados por vírgula

Separador por vírgula

1, 2, 3, 4, 5, 6

Separador por ponto e vírgula

1; 2; 3; 4; 5; 6

separador por espaço

1 2 3 4 5 6

# Possivel de se trabalhar, mas não é o ideal

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
     # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

A linguagem Python possui duas formas diferentes para ler dados em arquivos csv
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como Ordered Dicts

--------------------------------------------------------------------------------------------------------
# Reader

from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu em {linha [1]} e mede {linha[2]}')
"""

# DictReader

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um Ordered Dict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}")