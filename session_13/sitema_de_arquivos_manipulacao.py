"""
Sistema de Arquivos - Manipulação


# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arquivo.txt'))
print(os.path.exists('frutas.txt'))

# Diretório
print(os.path.exists('geek'))
print(os.path.exists('/home'))


# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()


# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass


# Criando arquivos

os.mknod('arquivos-teste4.txt')
os.mknod('/home/geek/university.txt')

# Se você estiver usando MacOS pode acontecer um erro de Permission

# OBS: Criando um arquivo via mknod() teremos um erro FileExistError

# Criando diretórios

os.mkdir('templates')

os.mkdir('/home/user/templates')

# OBS: a função mkdir() se este não existir se ele existir teremos FileExistError

# Criando multidiretórios (arvore de diretórios)

os.makedirs('templates/assets/images')


# Renomear diretórios

os.rename('templates', 'template')

# OBS: Se um diretório não existir teremos um FileNotFoundError

# OBS: Se um diretorio que queremos renomear não estiver vazio teremos um OSError

# Arquivos

os.rename('template/asstes/images/img1.png', 'logo.png')


# OBS: tome cuidado com a deleção de arquivos ou diretório, eles são deletados permanetemente e não
#passam pela 'lixeira'

os.remove('teste.txt')

# OBS: Caso o arquivo nã exista teremos o FileNotFoundError

# OBS: Se você informar um diretório ele apresentará um IsADirectoryError


# Removendo diretórios

os.rmdir('templates')

# OBS: Se o diretório tiver conteúdo teremos um OSError

# OBS: Se o diretório não existir teremos um FileNotFoundError


# Removendo uma árvore de arquivos

for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)
    if not arquivo.is_file():
        os.rmdir(arquivo.path)


# Podemos deletar uma árvore de diretórios vazios

os.removedirs()


# ATENÇÃO: Ao remover arquivos e diretórios com python eles não vão a lixeira eles vão ser apagados.

# Importando a biblioteca Send2Trash
from send2trash import send2trash -> envia arquivos e diretórios para a lixeira

os.remove('cesta1.txt')  # Não vai pra a lixeira

send2trash('cesta2.txt')  # Vai para a lixeira, podendo ser restaurado.

# OBS: Se o arquivo não existir teremos o OSError

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print('Criado arquivo temporário')
    with open(os.path.join(tmp, 'arquivotemp.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto, no final usamos um input para mantermos os
# arquivos temporários vivos dentros dos blocos with.

# Possivelmente não irá funcionar se você estiver usando o windows, pela sua forma de trabalhar
# com arquivos temporários.


import os
import tempfile

# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University \n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever em bits. Por isso, utilizamos b''

https://docs.python.org/3/library/os.html?highlight=os#module-os
"""

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Hello World\n')

print(arquivo.name)

print(arquivo.read())

input()

arquivo.close()