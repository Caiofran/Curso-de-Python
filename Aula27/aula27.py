#  Operador ternário em Python

# logged_user = True
# msg = "Usuário logado." if logged_user else 'Usuario precisa logar'
#
# print(msg)

# idade = 18
# idade = int(input("Digite sua idade: "))
idade = input("Digite sua idade: ")

if not idade.isnumeric():
    print('Você precisa digitar apenas números.')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'pode acessar' if e_de_maior else 'NÃO PODE ACESSAR.'

    print(msg)
