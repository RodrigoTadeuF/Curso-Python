"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do SO, precisamos importar
e fazer uso do módulo OS

os -> Operating System - Sistema Operacional

# getcwd() -> pega o current work directory - diretóriode trabalho corrente
# retorna o path absoluto
print(os.getcwd())

# Para mudar o diretório podemos usar o chdir()
os.chdir('..')

print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('/home/rodri')) # True

No windowns teremos que ter um cuidado maior e usar o caminho com \\
exemplo: C:\\Usuario\\pasta


# Podemos identificar o SO com o módulo os

print(os.name)  # Posix (Mac, Linux), nt (Windows)
print(os.uname())  # Mais informações

res = os.path.join(os.getcwd(), 'geek')
os.chdir(res)
#Join recebe dois parametros o diretorio atual e os que desejamos adicionar
"""

# Fazer import do os
import os

# Podemos listar os arquivos e diretórios com mais detalhes com o scandir()

scanner = os.scandir()
arquivos = list(scanner)

print(arquivos[0].inode())  # retorna o endereço da memória
print(arquivos[0].is_dir())  # retorna se é um diretório (boolean)
print(arquivos[0].is_file())  # retorna se é um arquivo (boolean)
print(arquivos[0].is_symlink())  # retorna se é um link simbólico (boolean)
print(arquivos[0].name)  # retorna o nome do arquivo
print(arquivos[0].path)  # retorna o caminho do arquivo
print(arquivos[0].stat())  # retorna estatísticas

#Precisamos fechar o scandir

scanner.close()

