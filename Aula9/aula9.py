"""
Entrada de dados - Aula 9
"""


nome = input("Qual o seu nome? \n")
idade = int(input("Qual é sua idade? \n"))
#  ano_nasc = 2020-int(idade)
ano_nasc = 2020-idade

print(f'\nMeu nome é {nome} \nMinha idade é: {idade} e o ano de nascimento é:{ano_nasc}')