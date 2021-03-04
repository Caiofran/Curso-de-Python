import os

caminho = r'D:\Downloads\Trabalho na Lymtech'
termo_procura = 'Login'
cont = 0

for raiz, diretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                cont += 1
                caminhp_completo = os.path.join(raiz, arquivo)
                size = os.path.getsize(caminhp_completo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                print('-' * 30)
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminhp_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', size)
            except FileNotFoundError:
                print('File not found.')
else:
    print('Nada encontrado.')