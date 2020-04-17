"""
Trabalhando com módulos Built-in (módulos integrados, que já vem instalados com o Python)

________________________
/Python/Modulos builtin/
----------------------

"""

# Utilizando alias (apelidos) para modulos/funções
import random as rdm

print(rdm.random())


# Podemos importar todas as funções de um módulo utilziando o *

from random import *

print(random())

# Importando todo o módulo

import random

print(random.random())

# Utilizando alias para as funções

from random import randint as rdi

print(rdi(5, 89))

# Podemos usar uma tupla para colocar múltiplos imports:
from random import shuffle, random, randint, choice

# prints...
