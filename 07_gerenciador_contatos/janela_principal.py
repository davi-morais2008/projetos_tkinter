import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class AppPrincipal:
    def __init__(self):
        self.janela = ttk.Window(themename="darkly")
        self.janela.title("Gestor de Contactos")
        self.janela.geometry("800x900+100+50")
        self.janela.resizable(False, False)

        # nome
        self.label_nome = ttk.Label(self.janela, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=10, pady=20)

        self.entry_nome = ttk.Entry(self.janela, width=40)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)
        
        #tel
        self.label_telefone = ttk.Label(self.janela, text="Telefone:")
        self.label_telefone.grid(row=1, column=0, padx=10, pady=20)

        self.entry_telefone = ttk.Entry(self.janela, width=40)
        self.entry_telefone.grid(row=1, column=1, padx=10, pady=5)

        #email
        self.label_email = ttk.Label(self.janela, text="Email:")
        self.label_email.grid(row=2, column=0, padx=10, pady=20)

        self.entry_email = ttk.Entry(self.janela, width=40)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        #moraada
        self.label_morada = ttk.Label(self.janela, text="Morada:")
        self.label_morada.grid(row=3, column=0, padx=10, pady=20)

        self.entry_morada = ttk.Entry(self.janela, width=40)
        self.entry_morada.grid(row=3, column=1, padx=10, pady=5)

        #botoes
        self.botao_add = ttk.Button(self.janela, width=15, text="Adicionar")
        self.botao_add.grid(row=4, column=0, padx=5, pady=40)

        self.botao_editar = ttk.Button(self.janela, width=15, text="Editar")
        self.botao_editar.grid(row=4, column=1, padx=5, pady=40)

        self.botao_remover = ttk.Button(self.janela, width=15, text="Adicionar")
        self.botao_remover.grid(row=4, column=2, padx=10, pady=40)
        
        self.tree = ttk.Treeview(
            self.janela,
            columns=("nome", "telefone", "email", "morada"),
            show="headings",
            bootstyle="dark"
        )
        self.tree.grid(row=5, column=0, columnspan=2, padx=38, pady=20)

        self.tree.heading("nome", text="Nome Completo")
        self.tree.heading("telefone", text="Telefone")
        self.tree.heading("email", text="Email")
        self.tree.heading("morada", text="Morada")

        self.tree.column("nome", width=200)
        self.tree.column("telefone", width=120)
        self.tree.column("email", width=200)
        self.tree.column("morada", width=200)

        self.tree.insert("", "end", values=["Davi", "9999-9999", "davi@email.com", "Araraquara"])
        self.tree.insert("", "end", values=["Rafael", "8888-8888", "rafael@email.com", "Matão"])
        self.tree.insert("", "end", values=["Levi", "7777-7777", "levi@email.com", "São Carlos"])



    def run(self):
        self.janela.mainloop()


if __name__ == "__main__":
    app = AppPrincipal()
    app.run()
