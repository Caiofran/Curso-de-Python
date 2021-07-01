import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXIST clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT'
               'peso REAL'
               ')')

cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Caio", 90.5)')
conexao.commit()

cursor.execute('SELECT * FROM cliente')

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()