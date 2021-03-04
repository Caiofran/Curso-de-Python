"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o
    valor da função2 executada
"""

# def funcao1(funcao_2):
#     return funcao_2
#
#
# def funcao2():
#     # var = 'Olá Mundo'
#     # return var
#     return 'Olá mundo'
#
#
# x = funcao1(funcao2())
#
# print(x)

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o 
    valor da função2 executada. Faça a função1 executar duas funções que 
    recebem um número diferente de argumentos.
"""


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


ex = mestre(fala_oi, 'Caio')

ex2 = mestre(saudacao, nome='Caio', saudacao='Olá')

print(ex)
print(ex2)
