"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#  num = input('Digite um número inteiro: ')
#
#  if not num.isdigit():
#      print('Isso não é um número inteiro')
#  else:
#      num = int(num)
#      if not num % 2 == 0:
#          print(f'O número {num} é impar')
#      else:
#          print(f'O número {num} é par')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#  num_hora = input('Informe um horário (0-23): ')
#
#  if num_hora.isdigit():
#      num_hora = int(num_hora)
#  if num_hora >=0 and num_hora <=11:
#      print('Bom Dia!!!')
#  elif num_hora >= 12 and num_hora <= 17:
#      print('Boa Tarde!!!')
#  elif num_hora >= 18 and num_hora <= 23:
#      print('Boa Noite!!!')
#  else:
#      print("Por favor, digite um horário entre 0 e 23.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome_primeiro = input('Digite seu primeiro nome: ')
num_letra = len(nome_primeiro)

if num_letra <= 4:
    print('Seu nome é curto')
elif num_letra >=5 and num_letra <=6:
    print('Seu nome é normal')
elif num_letra > 6:
    print("Seu nome é muito grande")
