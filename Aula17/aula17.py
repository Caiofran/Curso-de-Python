"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""
# positivos [012345678]
texto = 'Python s2'
# negativos   -[987654321]

# print(texto[8])

# nova_strings = texto[0::3]
# print(nova_strings)
print(len(texto))

for letra in texto:
    print(letra)
