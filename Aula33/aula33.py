"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
# def saudacao(saudacao, nome):
#     print(saudacao, nome)
#
# saudacao('Olá', 'Caio')
# saudacao('Hi', 'João')
# saudacao('Hello', 'Caio')
# saudacao('Oi', 'Caio')

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""

# def soma(a, b, c):
#     soma_num = a + b + c
#     print(f'A soma entre eles é: {soma_num}')
#
#
# soma(2, 4, 4)
# soma(1, 1, 3)
# soma(2, 1, 5)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""


# def funcao(n1, n2):
#     valor = n1
#     percentual = n2
#     novo_valor = valor + (valor * percentual / 100)
#     return novo_valor
#
#
# x = funcao(2, 10)
# print(x)
# x = funcao(20, 5)
# print(x)
# x = funcao(35, 10)
# print(x)

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""

# def divisivel(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return f'FizzBuzz, {num} é divisível por 3 e 5'
#     if num % 3 == 0:
#         return f'fizz, {num} é divisível por 3'
#     if num % 5 == 0:
#         return f'buzz, {num} é divisível por 5'
#     return num

# x = divisivel(81)
# print(x)
# x = divisivel(50)
# print(x)
# x = divisivel(1725)
# print(x)

# from random import  randint
#
# for i in range(100):
#     aleatorio = randint(0, 100)
#     print(divisivel(aleatorio))
