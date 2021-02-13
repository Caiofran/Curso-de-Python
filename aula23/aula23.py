"""
For / Else em Python
"""
variavel = ['Caio França', 'joãozinho', 'Maria']

comeca_com_j = False
for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'):
        print('Começa com J', valor)
        # comeca_com_j = True
        break
    # else:
    #     print('Não começa com J', valor)
# if comeca_com_j:
#     print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')
