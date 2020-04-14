"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: o raise não é uma função. É uma palavra reservada, bem como def ou outras em Python.

Para simplificar pense no raise como sendo útil para que possamos criar nossas prórias exceções e mensagens
de erro.

A forma geral de utilização é:

raise TipeDoErro('Mensagem de erro')

# Exemplo 1

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'o texto {texto} será impresso na cor {cor}')

colore('Geek', 'azul')

OBS: o raise, assim como return, finaliza uma função, ou seja, nada depois dele é executado.
"""

def colore(texto, cor):
    cores = ('verde', 'azul', 'amarelo', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if (cor) not in cores:
        raise ValueError(f'a cor precisa ser uma entre: {cores}')
    print(f'o texto {texto} será impresso na cor {cor}')

colore('Geek', 'azul')