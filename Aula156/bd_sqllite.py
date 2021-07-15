import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Caio", 90.5)')
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)', {'nome':'João', 'peso': 70})
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)', {'id': None, 'nome':'Daniel', 'peso': 25})
# conexao.commit()

# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',{'nome': 'Joana', 'id': 2})
# conexao.commit()

# cursor.execute('DELETE FROM clientes WHERE id=:id',{'id': 2})
# conexao.commit()

# cursor.execute('SELECT * FROM clientes')
# cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',{'peso': 50})

for linha in cursor.fetchall():
    # print(linha)

    # identificador, nome, peso = linha
    # print(identificador, nome, peso)
    nome, peso = linha
    print(nome, peso)

cursor.close()
conexao.close()