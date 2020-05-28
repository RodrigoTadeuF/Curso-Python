"""
JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre serviços oferecidos por empresas
(Twitter, Facebook, YT...) ou terceiros (nós desenvolvedores).

import json

ret = json.dumps(['produto', {'Playstation': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))
print(ret)
------------------------------------------------------------------------------------------------------------

import json

class Gato:
    def __init__(self, raca, nome):
        self.__raca = raca
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @property
    def nome(self):
        return self.__nome

felix = Gato('Felix', 'Vira-Lata')

ret = json.dumps(felix.__dict__)

print(ret)

Integrando o JSON com o pickle

pip install jsonpickle

ret = jsonpickle.encode(felix)
print(ret)

-------------------------------------------------------------------------------------------------------

# Escrevendo o arquivo json/pickle

import jsonpickle

class Gato:
    def __init__(self, raca, nome):
        self.__raca = raca
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @property
    def nome(self):
        return self.__nome

felix = Gato('Felix', 'Vira-Lata')

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)
"""

# Escrevendo o arquivo json/pickle

import jsonpickle

class Gato:
    def __init__(self, raca, nome):
        self.__raca = raca
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @property
    def nome(self):
        return self.__nome

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)