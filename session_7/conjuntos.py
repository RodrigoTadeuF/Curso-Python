"""
Conjuntos

 - Conjuntos em qualquer linguagem de programação, estamos fazendo referência a Teoria dos Conjuntos
 da Matemática.

 - Aqui no Python os conjuntos são chamados de Sets

 Dito isso, da mesma forma que na matemática:

 - Sets (Conjuntos) não possuem valores duplicados;
 - Sets (Conjuntos) não possuem valores ordenados;
 - Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens complicados.

Os conjuntos (sets) são referenciados em Python com {}

Diferença entre Conjuntos(Sets) e Mapas:
     - Um dicionário tem chave/valor;
     - Um conjunto tem apenas valor;

     # Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o três')
else:
    print('Não tem o três')

# Importante lembra que além de não ter valores duplicados, não temos ordem

# Listas aceitam valores duplicados
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionários: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar todos os tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente

for valor in s:
    print(valor)

# Usos interessantes com Sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu  os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetições

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas (únicas temos)

# O que você faria? Faria um loop na lista...?

# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
print(s)

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.remove(3)
print(s)
s.discard(2)
print(s)


# Copiando um conjunto para outro...

# Forma 1 = Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 = Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

s = {1, 2, 3}
print(s)

# Podemos remover todos os elementos de um conjunto

s.clear()
print(s)

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - usando PIPE

unicos2 = estudantes_python | estudantes_java

print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando Intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Métodos matemáticos de conjuntos

# Imagine que tenhamos dois conjuntos: Um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python estudam também Java.

# Gerar um conjunto de estudantes que não estão no outros

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

"""

