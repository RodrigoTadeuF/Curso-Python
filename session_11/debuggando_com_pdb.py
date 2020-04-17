"""
Debuggando com PDB

PDB -> Python Debugger


def dividir(a, b):
    try:
        return a / b
    except(ValueError, ZeroDivisionError) as err
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

import pdb

# comando basicos do PDB
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

nome = 'Rodrigo'
sobrenome = 'Tadeu'
pdb.set_trace()
nome_completo = nome + sobrenome
curso = 'Python Essencial'
final = nome_completo + 'fez o curso' + curso
print(final)

Podemos tambem usar o breakpoint()
"""

