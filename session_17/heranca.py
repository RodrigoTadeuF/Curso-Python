"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitamento de código, além de extender nossas classes.

OBS: Com a herança a partir de uma classe existente nós escrevemos outra classe que passa a herdar
atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente("Angelina", "Jolie", "123.456.789.00", 5000)
funcionario1 = Funcionario("Felicity", "Jones", "987.654.321-00", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente("Angelina", "Jolie", "123.456.789.00", 5000)
funcionario1 = Funcionario("Felicity", "Jones", "987.654.321-00", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())