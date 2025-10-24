import ttkbootstrap as ttk
from janela_lista import Lista_screen
import tkinter as tk
from tkinter import messagebox
from janela_lista import BancoDeDados



class Login():
    def __init__(self):

        self.db = BancoDeDados()


        self.janela = ttk.Window(themename="darkly")
        self.janela.geometry("600x600+100+50")
        self.janela.title("Lista de Afazeres")
        self.janela.resizable(False, False)
        self.iniciar()
        
    def iniciar(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
        # TITULO
        self.titulo = ttk.Label(self.janela, text="Realizando Login...", font=("Segoe UI", 16))
        self.titulo.place(relx=0.25, rely=0.2)
        # USUARIO
        self.label_user = ttk.Label(self.janela,
                                   text="Usuário")
        self.label_user.place(relx=0.29, rely=0.3 )
        self.entry_user = ttk.Entry(self.janela)
        self.entry_user.place(relx=0.29, rely=0.37)
        #SENHA
        self.label_senha = ttk.Label(self.janela,
                                    text="Senha",)
        self.label_senha.place(relx=0.29, rely=0.45)
        self.entry_senha = ttk.Entry(self.janela, show="•")
        self.entry_senha.place(relx=0.29, rely=0.52)
        #BOTÕES
        self.login_button = ttk.Button(self.janela, text="Login", width=5, command=self.verificar)
        self.login_button.place(relx=0.29, rely=0.63, width=175, height=50)
        self.register_button = ttk.Button(self.janela, text="Registrar", width=5, command=self.abrir_cadastro)
        self.register_button.place(relx=0.29, rely=0.74, width=175, height=50)


    def verificar(self):
        user = self.entry_user.get()
        senha = self.entry_senha.get()

        if user == "" or senha == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        usuario = self.db.cursor.execute(
            "SELECT * FROM usuarios WHERE nome=? AND senha=?", (user, senha)
        ).fetchone()

        if usuario:
            for widget in self.janela.winfo_children():
                widget.destroy()
                self.texto_login_efetuado = ttk.Label(self.janela, text="Login feito com sucesso!")
                self.texto_login_efetuado.place(relx=0.5, rely=0.5, anchor="center")
                self.return_button = ttk.Button(self.janela, text="Retornar a tela de login", command=self.iniciar)
                self.return_button.place(relx=0.5, rely=0.7, anchor="center")
                self.list_button = ttk.Button(self.janela, text="Abrir lista de tarefas", command=self.abrir_lista)
                self.list_button.place(relx=0.5, rely=0.6, anchor="center")
        else:
            self.erro_login = ttk.Label(self.janela, text="Usuário ou senha inválidos!")
            self.erro_login.place(relx=0.29, rely=0.75)

    def abrir_lista(self):
        self.janela.destroy()
        lista = Lista_screen()
        lista.run()

    def abrir_cadastro(self):
        self.cadastro = ttk.Toplevel(self.janela)
        self.cadastro.title("Cadastrar novo usuário")
        self.cadastro.geometry("400x300+200+150")
        self.cadastro.resizable(False, False)

        # Título
        ttk.Label(self.cadastro, text="Cadastro de Usuário", font=("Segoe UI", 14)).pack(pady=10)

        ttk.Label(self.cadastro, text="Usuário:").pack()
        entry_user = ttk.Entry(self.cadastro)
        entry_user.pack()

    
        ttk.Label(self.cadastro, text="Senha:").pack()
        entry_senha = ttk.Entry(self.cadastro, show="•")
        entry_senha.pack()

        def cadastrar():
            user = entry_user.get()
            senha = entry_senha.get()

            if user == "" or senha == "":
                messagebox.showerror("Erro", "Preencha todos os campos!")
                return

            existente = self.db.cursor.execute("SELECT * FROM usuarios WHERE nome=?", (user,)).fetchone()
            if existente:
                messagebox.showerror("Erro", "Usuário já existe!")
                return

            self.db.cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (user, senha))
            self.db.conn.commit()

            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.cadastro.destroy()

        # btao de cadastrar
        ttk.Button(self.cadastro, text="Cadastrar", command=cadastrar).pack(pady=15)


    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    bot = Login()
    bot.run()