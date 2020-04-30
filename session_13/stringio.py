"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do SO o software precisa ter permissão:
    - Permissão de leitura para ler o arquivo.
    - Permissão de escrita para escrever o arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória.
"""

# Primeiro fazemos o import
from io import StringIO

mensagem = 'Essa é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)

# Agora tendo o arquivo podemos utilizar tudo que já foi aprendido sobre arquivos
print(arquivo.read())

arquivo.write('U.U estamos desvendando o mundo de arquivos!')
arquivo.seek(0)

print(arquivo.read())