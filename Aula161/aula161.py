import sqlite3
# 162 163 164 165 pendete
class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')

    # Inserindo na Tabela
    # agenda.inserir('Caio', '123456')
    # agenda.inserir('Maria', '111111')
    # agenda.inserir('Luiz', '222222')
    # agenda.inserir('João', '333333')
    # agenda.inserir('Rose', '444444')
    # agenda.inserir('Guilherme', '555555')

    # Dando um update em uma linha
    # agenda.editar('Chico', '131313', '6')

    # Excluindo um linha
    # agenda.excluir(6)

    # Buscando no Banco de Dados
    # agenda.buscar('Rose')

    # agenda.listar()