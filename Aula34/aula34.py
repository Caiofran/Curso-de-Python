"""
Funções (def) em Python - *args **kwargs - (Parte 3)
"""
from typing import List


def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])
    # idade = kwargs.get('idade')
    idade = kwargs['idade']
    # print(nome)
    if idade is not None:
        print(idade)
    else:
        print("Idade não existe!!")
    # print(args[0])
    # print(args[-1])
    # print(len(args))


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Caio', sobrenome='França', idade=23)
