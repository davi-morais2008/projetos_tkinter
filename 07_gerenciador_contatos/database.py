import ttkbootstrap as ttk
import sqlite3

class BancoDeDados:
    def __init__(self, usuario_arquivo="07_gerenciador_contatos/contatos.db"):
        self.con = sqlite3.connect(usuario_arquivo)
        self.cursor = self.con.cursor()
        self.criar_table()


    def criar_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR (100) UNIQUE,
        telefone VARCHAR(15),
        email VARCHAR (40),
        morada VARCHAR (50),
        favorito INTEGER DEFAULT 0
        )""")
        self.con.commit()

    def adicionar(self, nome, telefone, email, morada):
        self.cursor.execute("INSERT INTO contatos (nome, telefone, email, morada) VALUES (?, ?, ?, ?)", (nome, telefone, email, morada))
        self.con.commit()

    def remover(self, nome):
        self.cursor.execute("DELETE from contatos WHERE nome = ?", (nome,))
        self.con.commit()

    def editar(self, id, nome_novo, telefone_novo, email_novo, morada_novo):
        self.cursor.execute("UPDATE contatos SET nome = ?, telefone = ?, email = ?, morada = ? WHERE nome = ?", (nome_novo, telefone_novo, email_novo, morada_novo, id))
        self.con.commit()

    def obter_contatos(self, nome=None):
        if nome:
            self.cursor.execute("SELECT nome, telefone, email, morada, concluido FROM contatos WHERE nome = ?", (nome,))
        else:
            self.cursor.execute("SELECT nome, telefone, email, morada FROM contatos")
        return self.cursor.fetchall()

    def favoritar(self, nome, favorito):
        self.cursor.execute("UPDATE contatos SET favorito = ? WHERE nome = ?", (favorito, nome))
        self.con.commit()
    def obter_favorito(self,nome):
        self.cursor.execute("SELECT favorito FROM contatos WHERE nome = ?", (nome,))
        return self.cursor.fetchone()[0]

    def fechar_conexao(self):
        self.con.close()
