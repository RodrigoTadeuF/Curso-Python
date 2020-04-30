"""
Escrevendo em arquivos

#OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele. Apenas ler.
Da mesma forma, se abrimos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

#OBS: Ao abrir um arquivo para escrita, o arquivo é criado no SO.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe um string como parâmetro.

Abrindo um arquivo para escrita com o modo 'w', s eo arquivo não existir será criado.
Caso ele já exista, o anterior sera apagado e um novo será criado. Dessa forma todo o
conteúdo no arquivo anterior é perdido.

arquivo = open('mais.txt', 'w')

arquivo.write('Algo por que testemas :P\n')
arquivo.write('Mais será que testamos tudo mesmo?')

arquivo.close()
"""

# Exemplo de escrita - modo Write -> w

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrevendo meu primeiro arquivo.\n')
    arquivo.write('Podemos dissertar na criação de arquivos.\n')
    arquivo.write('Enfim podemos nos divertir montando arquivos.')

