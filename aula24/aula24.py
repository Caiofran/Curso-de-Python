"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista #list
"""
# string = 'O Brasil é o o o pais do futebol, o Brasil é penta.'
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
#
# palavra = ''
# contagem = 0

# for valor in lista_1:
#     # print(f'A palavra ({valor}) apareceu ({lista_1.count(valor)}x) na frase.')
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

# for valor in lista_2:
#     print(valor.strip().capitalize())  # tira os espaços e capitalize deixa a primeira letra da frase maiuscula

# string = "O Brasil é penta."
# lista = string.split(' ')
# string2 = '.'.join(lista)  # serve para juntar elementos de uma lista
#
# print(string)
# print(lista)
# print(string2)

# string = "O Brasil é penta."
# lista = string.split(' ')
#
# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])

# lista = [
#     [1, 2],
#     [3, 4],
#     [5, 6],
# ]
#
# for v in lista:
#     print(v[0], v[1])

# lista = ['Caio', 'França', 'Ricciardi']

# for indice, nome in enumerate(lista):
#     print(indice, nome)

# Desempacotamento de listas
# n1, n2, n3 = lista
#
# print(n3, n2, n1)
