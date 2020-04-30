"""
Modos de abretura de arquivos

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve se o arquivo já existir
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista ele apresenta o
     FileExisistError
a -> Abre para escrita adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização: Leitura e escrita.

#OBS: Abrindo no modo a -> se o arquivo não existir ele será criado, caso ele já exista o novo conteúdo
será adicionado no final do arquivo SEMPRE.

http://docs.python.org/3/library/functions.html#open

# Exemplo 'x':

try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Agora fazemos coisas EXCLUSIVAS O.o/ \n')
except FileExistsError:
    print('O arquivo já existe')


# Exemplo 'a':

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

"""

with open('outro.txt', 'r+') as arquivo:
    arquivo.seek(0)
    arquivo.write('My place is at the TOP!\n')
    arquivo.write('Not anymore! \n')