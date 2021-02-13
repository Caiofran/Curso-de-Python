"""
*Criar variáveis para nome (str), idade (int),
*altura (float) e peso (float) de uma pessoa
*Criar variável com o ano atual (int)
*Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*Exbir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
nome = 'Caio'
idade = 23
altura = 1.83
peso = 80
ano_atual=2020
ano_de_nasc= ano_atual - idade
imc = peso/altura**2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é de {imc:.2f}.')
print(f'{nome} nasceu em {ano_de_nasc}.')
