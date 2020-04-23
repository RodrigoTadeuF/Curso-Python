"""
Dunder Name e Dunder Main

Dunder = Double under

Dunder Name -> __name__

Dunder Main -> __main__

Em Python são utilizados Dunder para criar funções atributos, propriedades etc. Utilizando
double under para não gerar conflito com os nomes desses elementos na programação

#Na linguagem C, temos um programa de seguinte forma:

int main() {
    return 0;
}

# Na linguagem Java temos um programa da seguinte forma:

public static void main(String[] args) {
}

# Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente o
Python atribuirá a variável __name__ o valor __main__ indicando que este módulo é o módulo de
execução principal.


"""