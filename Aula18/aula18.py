"""
While em Python
utilizado para realizar ações enquanto
uma condição for verdadeira.

Requisitos: Entender condições e operadores
"""
# x = 0
# while x < 10: # loop infinito
#     if x == 3:
#         # print(x)
#         x = x + 1
#         break
#     print(x)
#     x = x + 1
# print('Acabou!!')

# x = 0  # Coluna
#
# while x < 10:
#     y = 0  # linha
#     while y < 5:
#         print(f'({x}),({y})')
#         y += 1
#
#     # print(x)
#     x += 1

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja ? [s] ou [n]: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1-num_2)
    elif operador == '/':
        print(num_1/num_2)
    elif operador == '*':
        print(num_1*num_2)
    else:
        print('Operador inválido')


print('Acabou')
