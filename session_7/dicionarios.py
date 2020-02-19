"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas.

Dicionários são coleções do tipo chave/valor

[0, 1, 2] -> lista
[1, 2, 3]

(0, 1, 2) -> tupla
(1, 2, 3)

Em lista e tupla o par chave valor está implícito.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor'
    - Tanto a chave como o valor podem ser de qualquer tipo de dados
    - Podemos adicionar e misturar tipos de dados diferentes

    # Criação de dicionários

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['ru'])

# OBS: caso tentemos acessar uma chave que não existe teremos um Erro!

# Forma 2 - Acessando via get (Recomendável)

print(paises.get('br'))
print(paises.get('ru'))

paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py': 'Paraguai'}

pais = paises.get('br')

Caso o get não encontre o objeto que foi passado será retornado o valor None e não será gerado o valor KeyError

if pais:
    print(f'Encontrei o {pais}')
else:
    print('Não encontrei o pais')

# Podemos definir o valor padrão apra caso não encontremos o objeto com a chave informada
pais = paises.get('ru', 'Não encontrado')

print(f'encontrei o país: {pais}')


# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']


# Podemos utilziar qualquer tipo de dado ( int, String, boolean, float) incluisve (lista, tupla, dicionários) como
# chaves de dicionários

# Tuplas por exemplo são bastante interessantes para usar como chaves de dicionários pois as mesmas são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tokio',
    (40.7128, 74.8060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 - Mais comum
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}

receita.update(novo_dado)

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# CONCLUSÃO 1 a forma de adicionar ou alterar elementos em um dicionário são a mesma
# CONCLUSÃO 2 em dicionários NÃO podemos ter chaves repetidas

print(receita)
# Forma 1  -> Mais comum
ret = receita.pop('mar')
print(ret)

print(receita)
# OBS: Precisamos SEMPRE informar a chave e caso não encontre o elemento um KeyError é retornado.
# OBS2: Ao removermos o valor de um objeto o valor é sempre retornado

# Forma 2

del receita['fev']

print(receita)

# OBS: se a chave não existir será gerado um KeyError

"""

#Imagine que você tem um site de comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos

"""
Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2: 
        - nome;
        - quantidade;
        - preço;
        
        # 1 - Poderíamos utilizar uma Lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação no produto

# 2 - Poderiamos usar uma tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1 + produto2)

print(carrinho)

# Teriamos que saber qual é o índice de cada informação no produto

# - Poderiamos utilizar um Dicionário para isso? Sim

carrinho = []

produto1 = {'Nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'Nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma facilmente adicionamos ou removemos produtos do carrinho e em cada produto
# podemos ter a certeza sobre cada informação

#Limpar o dicionário (Zerar os dados)

d.clear()

print(d)



# Copiando um dicionário para outro

# Forma 1 Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4
print(novo)

# Forma 2 Shallow Copy

novo = d

print(novo)

novo['d'] = 4

"""

# Métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Forma não convencional de criação de dicionário

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parametros um iteravel e um valor.
# Ele vai gerar para cada valor do iteravel uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)