"""
Forçando tipos de de dados com decoradores

zip

a = (1, 2, 3)
b = (4, 5, 6)

c = zip(a,b)
(1,4), (2, 5), (3, 6)
"""

def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)
