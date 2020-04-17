"""
Try / Except / Else / Finally

Quando e onde tratar o código:

 - Toda entrada deve ser tratada!

OBS: Em muitos casos pode-se ter erros não esperados causados pelo usuário

# else -> É executado somente se não ocorrer o erro.

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto...")
else:
    print(f'Você digitou {num}')

# finally -> Esse bloco será sempre executado. Independente se houver exceção ou não.
# Geralmente é utilizado para fechar ou desalocar recursos

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Você não digitou um valor válido")
else:
    print(f'Você digitou o numero: {num}')
finally:
    print('Executando finally')

# Exemplo complexo - Não elegante

def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro número'))
try:
    num2 = int(input('Informe o segundo número'))
except ValueError:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo complexo - Não genérico

def dividir(a, b):
    try:
        return a / b
    except ValueError:
        return('Valor incorreto')
    except ZeroDivisionError:
        return ('Não podemos divir por zero')


num1 = int(input('Informe o primeiro número'))
num2 = int(input('Informe o segundo número'))

print(dividir(num1, num2))

# Exemplo complexo - Genérico

def dividir(a, b):
    try:
        return a / b
    except:
        return 'Ocorreu um erro'


num1 = int(input('Informe o primeiro número'))
num2 = int(input('Informe o segundo número'))

print(dividir(num1, num2))

"""
# Exemplo complexo - Semi-Genérico

def dividir(a, b):
    try:
        return a / b
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro {err}'


num1 = int(input('Informe o primeiro número'))
num2 = int(input('Informe o segundo número'))

print(dividir(num1, num2))