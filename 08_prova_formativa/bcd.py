import sqlite3

class BancoDeDados:
    def __init__(self, usuario_arquivo="08_prova_formativa/sorteio.db"):
        self.usuario_arquivo = usuario_arquivo
        self.con = sqlite3.connect(usuario_arquivo)
        self.cursor = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogadas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resultados TEXT NOT NULL
        )
        """)
        self.con.commit()
        self.con.close()

    def add_moves(self, resultado):
        self.con = sqlite3.connect(self.usuario_arquivo)
        self.cursor = self.con.cursor()
        self.cursor.execute("INSERT INTO jogadas (resultados) VALUES (?)", (resultado,))
        self.con.commit()
        self.con.close()


    def select_moves(self):
        self.con = sqlite3.connect(self.usuario_arquivo)
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT resultados FROM jogadas")
        dados = self.cursor.fetchall()
        self.con.close()
        return dados
    
    def clean_table(self):
        self.con = sqlite3.connect(self.usuario_arquivo)
        self.cursor = self.con.cursor()
        self.cursor.execute("DELETE FROM jogadas")
        self.con.commit()
        self.con.close()