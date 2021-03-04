#  Dicionários em Python

# d1 = {'chave1': 'Valor da chave1'}
# d1 = dict(chave1='Valor da chave1', chave2='Valor da chave2')
# d1 = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor real da chave.'}
# d1['chave2'] = 'Valor da chave2'

# d1 = {
#     'str': 'valor',
#     123: 'Outro valor',
#     (1, 2, 3, 4): 'tupla'
# }

# d1['str'] = "Agora ela existe."
# d1.update({'Nova_chave' : 'novo_valor'})

# print(d1['str'])
# if d1.get('Nova_chave'):
#     print(d1.get('Nova_chave'))

# del d1['str']

# print('str' in d1)
# print('valor' in d1.values())
# print(len(d1))

# d1 = {
#     'chave1': 'valor',
#     'chave2': 'Outro valor',
#     'chave3': 'tupla'
# }
#
# for k, v in d1.items():
#     print(k, v)

# clientes = {
#     'cliente1': {
#         'nome' : 'Caio',
#         'sobrenome' : 'França',
#     },
#     'cliente2': {
#         'nome' : 'João',
#         'sobrenome' : 'Moreira',
#     },
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')

# import copy
#
# d1 = {1: 'a', 2: 'b', 3: 'c', 'd' : ['CAIO', 'FRANÇA']}
# # v = d1
# # v = d1.copy()
# v = copy.deepcopy(d1)  # Cópia profunda
# v[1] = 'Caio'
# # v[2] = 'William'
# # print(v['d'][0])
# v['d'][0] = 'Joãozinho'
#
# print(d1)
# print(v)
# lista com dicionário e dados e valor
# lista
# lista = [
#     ['c1', 1],
#     ['c2', 2],
#     ['c3', 3],
# ]
# tupula
# lista = [
#     ('c1', 1),
#     ('c2', 2),
#     ('c3', 3),
# ]

# d1 = dict(lista)
# print(d1)

d1 = {
    1: 2,
    2: 3,
    4: 5,
}

# d1.pop(4)
# d1.popitem()

d2 = {
    'a': 'b',
    'c': 'd'
}

# print(d1)
# print(d2)

d1.update(d2)

print(d1)
