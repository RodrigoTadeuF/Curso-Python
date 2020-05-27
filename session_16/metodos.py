"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto, ou seja, as ações
que este objeto pode ralizar no seu sistema.

Em Python, dividimos os métodos, assim como os atributos em 2 grupos:
  - Métodos de instância;
  - Métodos de classe.

Métodos de instância

O método dunder init __init__ é um método especial chamado de construtor e
sua função é construir o objeto a partir da classe.

Os métodos/funções dunder em Python são chamados de métodos mágicos.

Por mais que possamos criar nossas próprias funções utilizando dunder não é aconselhado.
Python possui vários métodos com esta forma de nomenclatura pode ser que mudemos o
comportamento dessas funções mágicas internas da linguagem. Então evitemos ao máximo. Preferêncialmente
não fazendo.

Métodos são escritos em letras minúsculas. Se o nome for composto, o nome tera as palavras separadas por underline

"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """ retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuarios no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False



nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
email = input("Informe o e-mail: ")
senha = input("Informe a senha: ")
confirma_senha = input("Confirme a senha: ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(42)

print('Usuário criado com sucesso')

if user.checa_senha(senha):
    print('Acesso permitido')
else :
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}') # acesso errado