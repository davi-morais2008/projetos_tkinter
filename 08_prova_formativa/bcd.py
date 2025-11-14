import sqlite3

class BancoDeDados:
    def __init__(self, usuario_arquivo="08_prova_formativa/sorteio.db"):
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

    def add_moves(self, resultado):
        self.cursor.execute("INSERT INTO jogadas (resultados) VALUES (?)", (resultado,))
        self.con.commit()


    def select_moves(self):
        self.cursor.execute("SELECT resultados FROM jogadas")
        return self.cursor.fetchall()
    
    def clean_table(self):
        self.cursor.execute("DELETE FROM jogadas")
        self.con.commit()