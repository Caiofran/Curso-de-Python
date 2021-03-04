perguntas = {
    'Pergunta1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': 'b',
    },
    'Pergunta2': {
        'pergunta': 'Quanto é 3*2?',
        'respostas': {'a': '4', 'b': '10', 'c': '6', },
        'resposta_certa': 'c',
    },
    'Pergunta3': {
        'pergunta': 'Quanto é 1+2?',
        'respostas': {'a': '3', 'b': '10', 'c': '6', },
        'resposta_certa': 'a',
    },
    'Pergunta4': {
        'pergunta': 'Quanto é 1-1?',
        'respostas': {'a': '4', 'b': '0', 'c': '60', },
        'resposta_certa': 'b',
    },
    'Pergunta5': {
        'pergunta': 'Quanto é 8/4?',
        'respostas': {'a': '4', 'b': '10', 'c': '2', },
        'resposta_certa': 'c',
    },
}
print()

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EHHHH!!!! Você acertou!!!')
        respostas_certas += 1
    else:
        print('IXXIIIII!!! Você errou!!!!')

    print()

qtd_perguntas =  len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')
