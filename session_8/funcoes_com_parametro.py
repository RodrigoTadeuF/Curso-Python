"""
Funções com Parâmetros (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Em um programa qualquer geralmente temos:

entrada -> processamento -> saída

Em uma função temos:
 - Aquelas que não possuem entrada;
 - Aquelas que não possuem saída;
 - Aquelas que possuem entrada e não possuem saída;
 - Aquelas que possuem saída e não possuem entrada;
 - Aquelas que possuem entrada e saída;

# Refatorando uma função

def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')


print(cantar_parabens('Rodrigo'))


# Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgulas

# Exemplo

def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10,20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek'))
print(outra(5, 4, 'Python'))

# OBS: Se for informado um numero errado de parÂmetros ou argumentos, teremos um TypeError

# print(soma(2, 3, 4))  # Erro!
# print(soma(4))  # Erro!


# Nomeando parâmetros

def nome_completo(string1, string2):
    return f'Seu nome completo é {string1} {string2}'


print(nome_completo('Rodrigo', 'Tadeu'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem

print(nome_completo(nome='Rodrigo', sobrenome='Tadeu'))

"""

# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = 1, 2, 3, 4, 5, 6, 7
print(soma_impares(tupla))
