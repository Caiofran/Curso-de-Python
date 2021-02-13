"""
While / Else
contadores
acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break  # faz o loop interronper

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')
print('Cheguei no final fora do while.')
