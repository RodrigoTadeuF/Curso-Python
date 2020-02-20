"""
Módulo Collections - Default Dicts

# Recap Dicionarios

dicionario = { 'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # ?? Key Error

Default Dict -> Ao criar um dicionário utilizando-o, nós informaremos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuído.

OBS: Lambdas são funcções sem nome, que podem ou não receber parêmetros de entrada e retornar valores.
"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)
