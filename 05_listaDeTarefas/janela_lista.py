import tkinter as tk
import sqlite3
from tkinter import messagebox

class BancoDeDados:
    def __init__(self, usuario_arquivo="05_listaDeTarefas/tarefas.db"):
        self.conn = sqlite3.connect(usuario_arquivo)
        self.cursor = self.conn.cursor()
        self.criar_tabela()
        self.criar_tabela_usuarios()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                concluido INTEGER DEFAULT 0,
                usuario VARCHAR (20)
            )
        """)
        self.conn.commit()

    def criar_tabela_usuarios(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                usuario VARCHAR (20) PRIMARY KEY UNIQUE,
                senha TEXT NOT NULL
            )
        """)
        self.conn.commit()

    # cadastrar usuario
    def cadastrar_usuario(self, usuario, senha):
        try:
            self.cursor.execute("INSERT INTO usuarios (usuario,senha) VALUES (?, ?)", (usuario, senha))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def verificar_usuario(self, usuario, senha):
        self.cursor.execute("SELECT * FROM usuarios WHERE usuario=? and senha=?", (usuario, senha))
        return self.cursor.fetchone() is not None



    # funcoes das tarefas ---------------------------------------------------------
    def adicionar_tarefa(self, descricao, usuario):
        self.cursor.execute("INSERT INTO tarefas (descricao, usuario) VALUES (?, ?)", (descricao, usuario))
        self.conn.commit()

    def remover_tarefa(self, descricao):
        self.cursor.execute("DELETE FROM tarefas WHERE descricao = ?", (descricao,))
        self.conn.commit()

    def atualizar_status(self, descricao, concluido):
        self.cursor.execute("UPDATE tarefas SET concluido = ? WHERE descricao = ?", (concluido, descricao))
        self.conn.commit()

    def obter_tarefas(self, usuario):
        self.cursor.execute("SELECT descricao, concluido FROM tarefas WHERE usuario = ?", (usuario,))
        return self.cursor.fetchall()
    
    def fechar_conexao(self):
        self.conn.close()




class Lista_screen():
    def __init__(self, usuario):

        self.usuario = usuario
        self.db = BancoDeDados()


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
                                    text="Adicionar",
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
                                      text="Digite o usuario da tarefa: ",
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
        tarefas = self.db.obter_tarefas(self.usuario)
        for descricao, concluido in tarefas:
            status = "[x]" if concluido else "[ ]"
            self.listacaixa.insert(tk.END, f"{status} {descricao}")

    def adcionar_tarefa(self):
        tarefa = self.campo_tarefa.get()
        #se o campo estiver vazio, faz nada
        if tarefa == "":
            return
        #verifica se oq foi escrito no campo, ja existe na lista
        tarefas_existentes = self.db.obter_tarefas(self.usuario)
        for descricao, _ in tarefas_existentes:
            if descricao == tarefa:
                messagebox.showerror("Erro", "A tarefa digitada já está na lista.")
                return
        #adiciona normalmente caso nao exista
        self.db.adicionar_tarefa(tarefa, self.usuario)
        self.listacaixa.insert(self.listacaixa.size(), f"[ ] {tarefa}")
        self.campo_tarefa.delete(0, tk.END)

        
        
    def remover_tarefa(self):
        selecao = self.listacaixa.curselection()
        if selecao:
            index = selecao[0]
            tarefa = self.listacaixa.get(index)
            descricao = tarefa[4:] 
            self.db.remover_tarefa(descricao)
            self.listacaixa.delete(index)


    def concluir_tarefa(self):
        tarefa_selecionada = self.listacaixa.curselection()  
        if tarefa_selecionada:
            index = tarefa_selecionada[0]
            tarefa = self.listacaixa.get(index)
            descricao = tarefa[4:]  

            if str(tarefa).startswith("[ ]"):
                nova_tarefa = f"[x] {descricao}"
                concluido = 1
            elif str(tarefa).startswith("[x]"):
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