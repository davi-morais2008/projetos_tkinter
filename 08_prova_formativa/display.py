import ttkbootstrap as ttk
from tkinter import messagebox
from bcd import BancoDeDados
import random

lista_frutas = ["🍇", "🍉", "🍎", "🍒", "🍓"]

class AppPrincipal:
    def __init__(self):

        self.db = BancoDeDados()

        self.janela = ttk.Window(themename="darkly")
        self.janela.title("Sorteio de Frutas")
        self.janela.geometry("800x900+100+50")
        self.janela.resizable(False, False)

        self.label_titulo = ttk.Label(self.janela, text=" ? ", font=("Helvetica", 90), borderwidth=5, relief="solid")
        self.label_titulo.place(x=50, y=50)

        self.label_titulo2 = ttk.Label(self.janela, text=" ? ", font=("Helvetica", 90), borderwidth=5, relief="solid")
        self.label_titulo2.place(x=300, y=50)

        self.label_titulo3 = ttk.Label(self.janela, text=" ? ", font=("Helvetica", 90), borderwidth=5, relief="solid")
        self.label_titulo3.place(x=550, y=50)

        self.button_sorteio = ttk.Button(self.janela, text="Sortear", width=15, command=self.sorteio)
        self.button_sorteio.place(x=200, y=300)

        self.button_clean = ttk.Button(self.janela, text="Excluir", width=15, command=self.limpar_lista)
        self.button_clean.place(x=400, y=300)


        self.tree = ttk.Treeview(
            self.janela,
            columns=("jogadas"),
            show="headings",
        )
        self.tree.heading("jogadas", text="Jogadas")
        self.tree.column("jogadas", width=150, anchor="center")
        self.tree.place(x=0, y=380, width=770, height=500)

        self.scroll_y = ttk.Scrollbar(self.janela, orient="vertical", command=self.tree.yview)
        self.scroll_y.place(x=770, y=380, height=500)

        self.tree.configure(yscrollcommand=self.scroll_y.set)

        self.obter_jogadas()

    def obter_jogadas(self):
        jogadas = self.db.select_moves()
        for resultado in jogadas:
            self.tree.insert("", "end", values=(resultado))

    def sorteio(self):
        fruta1 = random.choice(lista_frutas)
        fruta2 = random.choice(lista_frutas)
        fruta3 = random.choice(lista_frutas)

        self.label_titulo.configure(text=fruta1)
        self.label_titulo2.configure(text=fruta2)
        self.label_titulo3.configure(text=fruta3)
        
        if fruta1 == fruta2 == fruta3:
            jogada = f"Vitoria: {fruta1}-{fruta2}-{fruta3}"
            self.tree.insert("", "end", values=(jogada,))
            self.db.add_moves(jogada)
            messagebox.showinfo("Vitória!", "🎉 Parabéns, você ganhou!")
        else:
            jogada = f"Jogada: {fruta1}-{fruta2}-{fruta3}"
            self.tree.insert("", "end", values=(jogada,))
            self.db.add_moves(jogada)

    def limpar_lista(self):
        self.tree.delete(*self.tree.get_children())
        self.db.clean_table()
        self.label_titulo.configure(text=" ? ")
        self.label_titulo2.configure(text=" ? ")
        self.label_titulo3.configure(text=" ? ")

    
    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = AppPrincipal()
    app.run()
