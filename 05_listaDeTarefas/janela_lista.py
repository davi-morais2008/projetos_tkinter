import tkinter as tk
import sqlite3


class BancoDeDados:
    def __init__(self, nome_arquivo="tarefas.db"):
        self.conn = sqlite3.connect(nome_arquivo)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                concluido INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def adicionar_tarefa(self, descricao):
        self.cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
        self.conn.commit()

    def remover_tarefa(self, descricao):
        self.cursor.execute("DELETE FROM tarefas WHERE descricao = ?", (descricao,))
        self.conn.commit()

    def atualizar_status(self, descricao, concluido):
        self.cursor.execute("UPDATE tarefas SET concluido = ? WHERE descricao = ?"(concluido, descricao))
        self.conn.commit()

    def obter_tarefas(self):
        self.cursor.execute("SELECT descricao, concluido FROM tarefas")
        return self.cursor.fetchall()
    
    def fechar_conexao(self):
        self.conn.close()






class Lista_screen():
    def __init__(self):
        self.db =BancoDeDados()

        self.janela = tk.Tk()
        self.janela.configure(bg= "#4e4d54")
        self.janela.geometry("800x600+100+50")
        self.janela.title("Lista de Tarefas")
        self.janela.resizable(True, True)

        self.titulo = tk.Label(self.janela,
                               text="Lista de Afazeres",
                               bg="#4e4d54",
                               fg="white",
                               font=("Segoe UI", 24))
        self.titulo.place(relx=0.05, rely= 0.01)

        self.item_lista = tk.Variable(value= [])

        self.listacaixa = tk.Listbox(listvariable=self.item_lista,
                                     font=("Segoe UI", 20),
                                     bg="darkblue",
                                     fg="white")
        self.listacaixa.place(relx=0.25, rely=0.52, anchor="center", height=500)

        # BOTÕES
        self.button_add = tk.Button(self.janela,
                                    bg="lightblue",
                                    text="Adcionar",
                                    font=("Segoe UI", 18),
                                    fg="white",
                                    width=30,
                                    height=7,
                                    command=self.adcionar_tarefa)
        self.button_add.place(
                                    width=200,   
                                    height=60,   
                                    relx=0.63,
                                    rely=0.18,
                                    anchor="center"
                                )

        # REMOVE
        self.button_remove = tk.Button(self.janela,
                                       text="Remover",
                                       font=("Segoe UI", 18),
                                    bg="lightblue",
                                    fg="white",
                                    command=self.remover_tarefa)
        self.button_remove.place(
                                    width=200,   
                                    height=60,   
                                    relx=0.63,
                                    rely=0.31,
                                    anchor="center"
                                )

        #CONCLUIR
        self.button_concluir = tk.Button(self.janela,
                                         text="Concluir",
                                         font=("Segoe UI", 18),
                                    bg="lightblue",
                                    fg="white",
                                    command=self.concluir_tarefa)
        self.button_concluir.place(
                                    width=200,   
                                    height=60,   
                                    relx=0.63,
                                    rely=0.44,
                                    anchor="center"
                                )
        
        self.texto_inserir = tk.Label(self.janela,
                                      text="Digite o nome da tarefa: ",
                                      font=("Segoe UI", 18),
                                      fg="white",
                                      bg="#4e4d54")
        self.texto_inserir.place(rely=0.55, relx=0.5)

        self.campo_tarefa = tk.Entry(self.janela, font=("Segoe UI", 14))
        self.campo_tarefa.place(rely=0.63, 
                                relx=0.5,
                                width=350,
                                height=30)
        

        self.carregar_tarefas()

        # Garante que o banco será fechado ao sair
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar)


    def carregar_tarefas(self):
        tarefas = self.db.obter_tarefas()
        for descricao, concluido in tarefas:
            status = "[x]" if concluido else "[ ]"
            self.listacaixa.insert(tk.END, f"{status} {descricao}")

    def adcionar_tarefa(self):
        tarefa = self.campo_tarefa.get()
        if tarefa != "":
            self.db.adicionar_tarefa(tarefa)
            self.listacaixa.insert(self.listacaixa.size(), f"[ ] {tarefa}")

    def remover_tarefa(self):
        selecao = self.listacaixa.curselection()
        if selecao:
            index = selecao[0]
            tarefa = self.listacaixa.get(index)
            descricao = tarefa[4:]  # Remove o "[ ] " ou "[x] "
            self.db.remover_tarefa(descricao)
            self.listacaixa.delete(index)


    def concluir_tarefa(self):
        tarefa_selecionada = self.listacaixa.curselection()  
        if tarefa_selecionada:
            index = tarefa_selecionada[0]
            tarefa = self.listacaixa.get(index)
            descricao = tarefa[4:]  # Remove "[ ] " ou "[x] "

            if tarefa.startswith("[ ]"):
                nova_tarefa = f"[x] {descricao}"
                concluido = 1
            elif tarefa.startswith("[x]"):
                nova_tarefa = f"[ ] {descricao}"
                concluido = 0

            self.db.atualizar_status(descricao, concluido)
            self.listacaixa.delete(index)
            self.listacaixa.insert(index, nova_tarefa)
    def fechar(self):
        self.db.fechar_conexao()
        self.janela.destroy()


    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    bot = Lista_screen()
    bot.run()