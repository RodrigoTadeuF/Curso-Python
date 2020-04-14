"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo
assim que o programa pare de funcionar e o usuário recebe mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    // execução problemática
except:
    // o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro comum

try:
    geek()
except:
    print('Ocorreu um erro inesperado...')

OBS: Tratar o erro de forma genérica não é o ideal, o correto é se tratar de forma específica
------------------------------------------------------------------------
# Exemplo 2 - Tratando um erro de forma específica

try:
    geek()
except NameError:
    print('Ocorreu um erro inesperado...')
------------------------------------------------------------------------
# Exemplo 2 - Tratando um erro de forma específica com detalhes do erro

try:
    geek()
except NameError as err:
    print(f'Ocorreu um erro inesperado do tipo {err}')
------------------------------------------------------------------------
# Exemplo 3 - Podemos tratar vários erros de uma única vez

try:
    len(5)
except NameError as erra:
    print(f'Deu NameError {erra}')
except TypeError as err:
    print(f'Deu TypeError {err}')

"""

def pega_valor(dict, key):
    try:
        return dict[key]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Rodrigo"}

print(pega_valor(dic, "asd"))