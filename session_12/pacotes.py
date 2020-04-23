"""
Pacotes:

Módulo -> É apenas um arquivo Python que pode ter diversas funções que podemos utilizar;

Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x um pacote Python deveria conter dentro dele um arquivo
chamado __init__.py

Nas versões do Python 3.x não é mais obrigatória a utilização deste arquivo, mas
normalmente ainda é utilizado para manter a compatibilidade.
"""

from geek import geek1, geek2

from geek.univesity import geek3, geek4

print(geek1.pi)

print(geek1.funcao1(4, 6))

print(geek2.curso)

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())