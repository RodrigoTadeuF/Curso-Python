"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilziamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização, nós passamos apenas um parâmetro de entrada,
que neste caso é o caminho para o arquivo a ser lido do arquivo a ser lido. Essa função retorna um
_io.TextIoWrapper e é com ele que trabalhamos.

https://docs.python.org/3/library/functions.html#open

# OBS: por padrão a função open abre o arquivo para leitura. Este arquivo deve existir ou
então teremos o erro FileNotFoundError.

mode 'r' -> 'read'
"""

# Exemplo

arquivo = open("texto.txt")

# print(arquivo)

# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após a sua abertura, devemos utilizar a função read()

print(arquivo.read())

# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor
#funciona como o cursor quando estamos escrevendo.

# OBS: A função read le todo o conteúdo do arquivo
