import tkinter as tk

class Login_screen():
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.configure(bg= "#4e4d54")
        self.janela.geometry("800x600+100+50")
        self.janela.title("A Porra de uma tela de Login")
        self.janela.resizable(True, True)

        self.titulo = tk.Label(self.janela,
                               text="Lista de Afazeres",
                               bg="#4e4d54",
                               fg="white",
                               font=("Segoe UI", 24))
        self.titulo.place(relx=0.05, rely= 0.01)

        self.item_lista = tk.Variable(value= [
    {1: "almocar"},
    {2: "estudar"},
    {3: "ler"},
    {4: "correr"},
    {5: "dormir"},
    {6: "trabalhar"},
    {7: "limpar"},
    {8: "comprar"},
    {9: "cozinhar"},
    {10: "meditar"}
])
        self.listacaixa = tk.Listbox(listvariable=self.item_lista,
                                     width=50,
                                     heigh=23)
        self.listacaixa.place(relx=0.25, rely=0.44, anchor="center")

        # BOTÕES
        self.button_add = tk.Button(self.janela,
                                    bg="lightblue",
                                    text="Adcionar",
                                    font=("Segoe UI", 18),
                                    fg="white",
                                    width=30,
                                    height=7)
        self.button_add.place(
                                    width=200,   
                                    height=60,   
                                    relx=0.82,
                                    rely=0.17,
                                    anchor="center"
                                )

        # REMOVE
        self.button_remove = tk.Button(self.janela,
                                       text="Remover",
                                       font=("Segoe UI", 18),
                                    bg="lightblue",
                                    fg="white")
        self.button_remove.place(
                                    width=200,   
                                    height=60,   
                                    relx=0.82,
                                    rely=0.30,
                                    anchor="center"
                                )

        #CONCLUIR
        self.button_concluir = tk.Button(self.janela,
                                         text="Concluir",
                                         font=("Segoe UI", 18),
                                    bg="lightblue",
                                    fg="white",)
        self.button_concluir.place(
                                    width=200,   
                                    height=60,   
                                    relx=0.82,
                                    rely=0.7,
                                    anchor="center"
                                )
        
        self.texto_inserir = tk.Label(self.janela)












    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    bot = Login_screen()
    bot.run()