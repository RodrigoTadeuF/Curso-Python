"""
Decoradores (Decorators)

O que são Decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de HOF;
- Decorators tem uma sintaxe própria, usando '@' (Syntact Sugar/ Açúcar sintático)


# Decorators como funções (Sintaxe não recomendado

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia')
    return sendo

def saudacao():
    print('Seja bem vindo(a) a nossa casa!')

# Testes

teste = seja_educado(saudacao)

teste()

# Testando 2

def raiva():
    print('EU TE ODEIO')

raiva_educada = seja_educado(raiva)

raiva_educada()

# Decorators com Syntax Sugar

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


apresentando()

@seja_educado_mesmo
def dormir():
    print('Quero dormir')


dormir()

"""

