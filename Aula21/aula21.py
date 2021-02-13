"""
For in em Python
Iterando strings com for
Função rage(start=0, stop, step=1)
"""
# texto = 'Python'
#
# for letra in texto:
#     print(letra)
# for num in range(0, 100, 8):
#     print(num)
texto = 'Python'
nova_string = ''

# continue - pula para o proximo laço
# break - termina o laço

for letra in texto:
    if letra == 't':
        # continue
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        # break
    else:
        nova_string += letra
print(nova_string)
