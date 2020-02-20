"""
Funções com Parâmetros Padrão (Default Paramters)

- Funções onde a passagem de parÂmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional

print('Geek University')

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TypeError



def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))  # Por padrão eleva ao quadrado
print(exponencial(3, 5))  # Eleva a potencia informada pelo usuário

# OBS
# Se o usuário passar somente 1 parâmetro, este será atribuido ao parâmetro numero, e será calculado o quadrado deste
# numero.
# Se o usuário passar 2 argumentos, o primeiro será atribuído ai oarâmetro número e o segundo ao parâmetro potência.
# Então será calculada esta potência.

print(exponencial())


# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar no final da declaração

def teste(potencia, num=2):
    return  num ** potencia

print(teste(6))

# Outros exemplos

def soma(x1=5, x2=3):
    return x1 + x2


print(soma(4,3))
print(soma(4))
print(soma())

# Exemplo mais complexo

def mostra_informação(nome='Geek', instrutor=false):
    if nome == 'Geek' and instrutor:
        return 'Bem-Vindo instrutor Geek!'
    elif nome =='Geek':
        return 'Eu pensei que você era instrutor!'
    return f'Olá, {nome}'


print(mostra_informação())
print(mostra_informação(instrutor=True))
print(mostra_informação('Ozzy'))

# Por quê usar parâmetros com valor default?

-  Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legiveis de código;

# Quais tipos de dados podemos utilizar como valores default de parâmetros?

- Qualquer tipo de dado
    - Numeros, strings, floats, listas, tuplas .... etc

# Exemplos


def soma(x1, x2):
    return x1 + x2


def mat(n1, n2, fun=soma):
    return fun(n1, n2)


def subtracao(x1, x2):
    return x1 - x2


print(mat(2, 3))
print(mat(2, 2, subtracao))


# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'   # Variável global

def diz_oi():
    instrutor = 'Python'
    return f'Oi {instrutor}'


print(diz_oi())

# OBS: se tivermos uma variável local com o memso nome de uma variável global ela sobreporá a global.


def diz_oi():
    prof = 'Geek'   # Variável local
    return f'Olá {prof}'


print(diz_oi())

print(prof)  # NameError!

# ATENÇÃO com variáveis globais (se puder evite)

total = 0

def incrementa():
    total = total - 1  # Erro!
    return total


print(incrementa())


total = 0

def incrementa():
    global total
    total = total - 1
    return total


print(incrementa())

# Podemos ter funções dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())

"""

