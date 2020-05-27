"""
POO - Atributos

Atributos -> Representam as características do Objeto. Ou seja pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em python dividimos os atributos em três grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos.

# Atributos de instância: São atributos declarados dentro do método construtor

OBS: Método construtor é um método especial utilizado para a construção do objeto.

Em java uma classe lampada incluindo seus atributos ficaria mais ou menos:

public class Lampada() {
    private int voltagem;
    private String cor;
    private boolean ligada;

    public Lampada(int voltagem, String cor, boolean ligada){
        this.voltagem = voltagem;
        this.cor = cor;
        this.ligada = ligada;
    }
}

# O que signfica atributos de instância?

# Significa, que ao criarmos instância/objetos de uma classe, todas as instâncias
# terão estes atributos.

user1 = Acesso("user1@gmail.com", "1123456")
user2 = Acesso("user2@gmail.com", "654321")

print(user1.get_email())
print(user2.get_email())

# Atributos de Classe

# Atributos de classe, são atributos, claro, que são declarados diretamente na classe,
# ou seja, fora do construtor. Geralmente já inicializamos um valor, e este é compartilhada entre
# todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter
# seus próprios valores como é o caso dos atributos de instância, com os atributos de classe
# todas as instâncias terão o mesmo valor para este atributo
"""

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

'''    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def ligada(self):
        return self.__ligada


Em Python por convenção foi estabelecido que todo o atributo de uma classe é publico, ou seja,
pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está sendo declarado,
utiliza-se duplo __ underscore no início de seu nome

isso é conhecido como Name Mangling.
'''

# Classes com atributos públicos

class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.numero = numero


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Classes com atributos privados

class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

# Refatorar a classe Produto
class Produto:
    # Atributo de classe
    imposto = 1.05  # 5% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

# Atributos Dinâmicos -> Um atributos de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 2300)

p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)