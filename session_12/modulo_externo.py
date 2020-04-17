"""
Módulos Externos

# Utilizamos o gerenciados de pacotes Python chamado pip - Python Installer Package

https://pypi.org

colorama -> Utilizado para permiti impressão de textos coloridos no terminal

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')

"""

import pydf

pdf = pydf.generate_pdf('<h1> Geek University </h1></br></br><strong>Programa&ccedil;&atildeo Python: Essencial </strong>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

