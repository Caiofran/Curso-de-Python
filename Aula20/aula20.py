#        Índices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
# print(tamanho_frase)
# print(frase[:6])

input_do_usuario = input('Qual letra deseja colocar maiúscula: ')
#  interação
while contador < tamanho_frase:
    # print(frase[contador], contador)
    # nova_string += frase[contador]
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1
    # print(nova_string)

print(nova_string)