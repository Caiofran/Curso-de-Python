"""
Funções - def em Python (Parte 1)
"""


def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('O', '3')
    msg = msg.replace("u", '3')
    return f'{msg} {nome}'


v = saudacao()
print(v)
