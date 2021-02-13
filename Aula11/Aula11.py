"""
Operadores Relacionais
== > >= < <= !=
"""

#  num_1 = 2
#  num_2 = 2
#
#  expressao = (num_1 >= num_2)
#
#  print(expressao)

nome = input('Qual o seu nome? \n')
idade = int(input('Qual a sua idade? \n'))
#  idade = input('Qual a sua idade? \n')

#  Limite para pegar empréstimo
#  idade_limite = 18
idade_menor = 20  # muito jovem
idade_maior = 30  # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')
