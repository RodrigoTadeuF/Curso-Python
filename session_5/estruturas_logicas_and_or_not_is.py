"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    not, is
Operadores binários:
    and, or

Para o and ambos os valores precisam ser True
Para o or um ou outro valor precisam ser True
Para o not, o valor do booleano é invertido, ou seja, se for True vira False, se for False vira True
Para o is, o valor é comparado com o segundo
"""

ativo = False
logado = False

if not ativo:
    print('Você precisa ativar sua conta. Por favor cheque seu e-mail')
else:
    print('Bem vindo usuário')

# ativo é verdadeiro?
print(ativo is True)
