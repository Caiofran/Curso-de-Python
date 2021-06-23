"""
Pilhas e filas
Pilhas (stack) - FIFO - last in, first out.
    Exemplo: Pilha de livros que são adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item
alterado, todos os índices serão modificados.
alterado, todos os índices serão modificados.
"""

# livros = list()
# livros.append('Livro 1') # 1
# livros.append('Livro 2') # 2
# livros.append('Livro 3') # 3
# livros.append('Livro 4') # 4
# livros.append('Livro 5') # 5
# print(livros)
# livros_removido = livros.pop()
# livros_removido = livros.pop()
# livros_removido = livros.pop()
# livros_removido = livros.pop()
# livros_removido = livros.pop()
# print(livros, livros_removido)

from collections import deque
from time import sleep

# fila = deque()
# fila.append('Caio')
# fila.append('Maria')
# fila.append('Marcos')
# fila.append('Joãozinho')
#
# print(f'Saiu: {fila.popleft()}')
# print(f'Saiu: {fila.popleft()}')
#
# for nome in fila:
#     print(nome)

fila = deque(maxlen=10)
fila.extend([1, 2, 3, 4, 5, 6])
# fila.insert(2, 'Caio')
# fila.index()
fila.rotate(1)
print(fila)
# fila.append(5)
# fila.append(6)
# fila.append(7)

# for i in range(1000):
#     fila.append(i)
#     sleep(1)
#     print(fila)
