"""
Formatando valores com modificadores

:s - Texto(Strings)
:d - Inteiros (int)
:f - Números de pontos flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
# num_1 = 10
# num_2 = 3
# divisao = num_1 / num_2
# print('{:.2f}'.format(divisao))
# print(f'{num_1:2<10}')

# nome = 'Caio França'
# nome = nome.ljust(20, '#')
nome = 'Caio França'
print(nome.lower())  # tudo minusculo
print(nome.upper())  # tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas

