"""
Geradores

- Geradores (Generators) são Iteradores (Iterators);
- O contrário não é verdadeiro, ou seja nem todo Iterator é um Generator.

Outras infos:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenção entre funções e Generator Functions (Funções Geradoras)

-------------------------------------------------------------------------------
| Funções                            |  Generator Function                    |
-------------------------------------------------------------------------------
| Utilizam return                    | Utilizam yield                         |
| Retorna uma vez                    | Pode utilizar yield múltiplas vezes    |
| Quando executada, retorna um valor | Quando executada, retorna um Generator |
-------------------------------------------------------------------------------

# OBS: Uma Generator Function não é um Generator. Ela gera um Generator.

gen = conta_ate(5)

# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

"""

# Exemplo de Generator Function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


gen = conta_ate(10)

for num in gen:
    print(num)