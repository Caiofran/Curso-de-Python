usuario = input('Nome de Usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'caio'
senha_bd = '1234'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')
