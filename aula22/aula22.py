"""
Lista em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#         0    1    2    3    4    5
# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
#      -  6    5    4    3    2     1

# lista[5] = 'Qualquer outra coisa'

# print(lista[1:4])

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l1.extend(l2)
# l2.append('b')  # inseri no final da lista
# l2.insert(0, 'oi')  # inderi de acordo com o indice
# l2.pop()
# print(l2)
# print(l2[0])

# print(l1)
# print(l2)

#     0  1  2  3  4  5  6  7  8
# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l2)
# l2.insert(0, 'banana')
# print(l2)
# del(l2[0])
# print(l2)

# print(max(l2))
# print(min(l2))

# l2 = list(range(1, 10))
# # print(l2)
# soma = 0
#
# for valor in l2:
#     soma += valor
# print(soma)

l2 = ['String', True, 10, -20.5]

for elem in l2:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')
