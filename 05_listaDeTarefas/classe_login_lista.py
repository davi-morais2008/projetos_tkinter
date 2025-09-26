import ttkbootstrap as tk
from janela_lista import Lista_screen


usuarios = {
    "morais": "0000",
    "admin": "1234",
    "joao": "senha",
    "maria": "teste123"
}


class Login():
    def __init__(self):
        self.janela = tk.Window(themename="darkly")
        self.janela.geometry("600x600+100+50")
        self.janela.title("A Porra de uma tela de Login")
        self.janela.resizable(False, False)
        self.iniciar()
        
    def iniciar(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
        # TITULO
        self.titulo = tk.Label(self.janela, text="Realizando Login...", font=("Segoe UI", 16))
        self.titulo.place(relx=0.25, rely=0.2)
        # USUARIO
        self.label_user = tk.Label(self.janela,
                                   text="Usuário")
        self.label_user.place(relx=0.29, rely=0.3 )
        self.entry_user = tk.Entry(self.janela)
        self.entry_user.place(relx=0.29, rely=0.37)
        #SENHA
        self.label_senha = tk.Label(self.janela,
                                    text="Senha",)
        self.label_senha.place(relx=0.29, rely=0.45)
        self.entry_senha = tk.Entry(self.janela, show="•")
        self.entry_senha.place(relx=0.29, rely=0.52)
        #BOTÕES
        self.login_button = tk.Button(self.janela, text="Login", width=5, command=self.verificar)
        self.login_button.place(relx=0.29, rely=0.63, width=175, height=50)


    def verificar(self):
        
        user = self.entry_user.get()
        senha = self.entry_senha.get()

        if user in usuarios and usuarios[user] == senha:
            for widget in self.janela.winfo_children():
                widget.destroy()
                self.texto_login_efetuado = tk.Label(self.janela, text="Login feito com sucesso!")
                self.texto_login_efetuado.place(relx=0.5, rely=0.5, anchor="center")
                #botao voltar a tela de login
                self.return_button = tk.Button(self.janela,text="Retornar a tela de login", command= self.iniciar)
                self.return_button.place(relx=0.5, rely=0.7, anchor="center")
                #botao de abrir lista de afazeres
                self.list_button = tk.Button(self.janela,text="Abrir lista de tarefas", command= self.abrir_lista)
                self.list_button.place(relx=0.5, rely=0.6, anchor="center")
        else:
            self.erro_login = tk.Label(self.janela, text="Usuário ou senha inválidos!")
            self.erro_login.place(relx=0.29, rely=0.75)

    def abrir_lista(self):
        self.janela.destroy()
        lista = Lista_screen()
        lista.run()


    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    bot = Login()
    bot.run()