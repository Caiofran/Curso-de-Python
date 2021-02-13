"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# num_inteiro = input('Digite um número inteiro: ')
#
# if not num_inteiro.isdigit():
#     print('Isso não é um número inteiro')
# else:
#     num_inteiro = int(num_inteiro)
#     if not num_inteiro % 2 == 0:
#         print(f'O número {num_inteiro} é ímpar')
#     else:
#         print(f'O número {num_inteiro} é par')
#
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# num_horario = input('Digite uma horario entre (0-23): ')
#
# if num_horario.isdigit():
#     num_horario = int(num_horario)
#     if num_horario < 0 or num_horario > 23:
#         print("Horário deve estar entre 0 e 23")
#         if num_horario >= 0 and num_horario <= 11:
#             print('Bom dia!!!')
#         elif num_horario >=12 and num_horario <= 17:
#             print('Boa tarde!!!')
#         elif num_horario >= 18 and num_horario <= 23:
#             print('Boa noite!!!')
# else:
#     print("Por favor, digite um horário entre 0 e 23.")
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# num_nome = input('Informe seu primeiro nome: ')
# num_letra = len(num_nome)
#
# if num_letra <= 4:
#     print("Seu nome é curto")
# elif num_letra >= 5 and num_letra <= 6:
#     print("Seu nome é normal")
# elif num_letra > 6:
#     print("Seu nome é muito grande")
