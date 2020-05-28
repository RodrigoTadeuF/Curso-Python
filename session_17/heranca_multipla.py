"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de múltiplas classes
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por multiderivação Direta
    - Por multiderivação Indireta


# Exemplo 1
#Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Multiderivada(Base1, Base2):
    pass


# Exemplo 2
# Multiderivador Indireto

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass

OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança herdará
todos os atributos e métodos das super classes.
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} esta nadando'

    def cumprimentar(self):
        return f' Eu sou {self._Animal__nome} do mar'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'

class Penguim(Terrestre, Aquatico):

    def __int__(self, nome):
        super().__init__(nome)

# Testando

baleia = Aquatico('wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Penguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # Caso de MRO - Method Resolution Order

