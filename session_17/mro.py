"""
POO -> MRO - Method Resolution Order

Em Python podemos conferir a ordem de execução dos métodos de 3 formas:
    - Via propriedade da classe
    - Via método
    - Via help
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

tux = Penguim('Tux')
print(tux.cumprimentar())

"""
Method Resolution Order -> é a ordem de execução dos métodos, ou seja, quem será executado primeiro
"""