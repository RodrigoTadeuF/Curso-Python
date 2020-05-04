"""
Teste de Memória com Generators

Sequencia de Fibonacci
1, 1, 2, 3, 5, 8, 13...
"""

# 443MB
def fibonacci(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = a + b
    return nums


# Teste:
for n in fibonacci(100):
    print(n)

# Função usando geradores

def fibonacci_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste geradores 3MB
