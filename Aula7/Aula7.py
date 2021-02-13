nome = 'Caio França'
idade = 23
altura = 1.83
e_maior = idade > 18
peso = 80
imc = peso/altura**2

print(nome, 'tem', idade, 'de idade e seu IMC é:', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
print('{0} tem {1} anos e seu IMC é {2}'.format(nome, idade, imc))
