import ttkbootstrap as ttk
from database import BancoDeDados
from tkinter import messagebox

class AppPrincipal:
    def __init__(self):

        self.db = BancoDeDados()

        self.janela = ttk.Window(themename="darkly")
        self.janela.title("Contatos")
        self.janela.geometry("800x900+100+50")
        self.janela.resizable(False, False)

        self.label_titulo = ttk.Label(self.janela, text="Gerenciador", font=("Helvetica", 20))
        self.label_titulo.place(x=550, y=50)
        self.label_titulo2 = ttk.Label(self.janela, text="de", font=("Helvetica", 20))
        self.label_titulo2.place(x=615, y=110)
        self.label_titulo3 = ttk.Label(self.janela, text="Contatos", font=("Helvetica", 20))
        self.label_titulo3.place(x=570, y=170)

        #nome
        self.label_nome = ttk.Label(self.janela, text="Nome:", font=("Helvetica", 16), foreground="#316C9C")
        self.label_nome.place(x=50, y=50)

        self.entry_nome = ttk.Entry(self.janela, width=40)
        self.entry_nome.place(x=150, y=50)
        
        #tel
        self.label_telefone = ttk.Label(self.janela, text="Telefone:", font=("Helvetica", 16), foreground="#316C9C")
        self.label_telefone.place(x=50, y=110)

        self.entry_telefone = ttk.Entry(self.janela, width=40)
        self.entry_telefone.place(x=150, y=110)

        #email
        self.label_email = ttk.Label(self.janela, text="Email:", font=("Helvetica", 16), foreground="#316C9C")
        self.label_email.place(x=50, y=170)

        self.entry_email = ttk.Entry(self.janela, width=40)
        self.entry_email.place(x=150, y=170)

        #moradad
        self.label_morada = ttk.Label(self.janela, text="Morada:", font=("Helvetica", 16), foreground="#316C9C")
        self.label_morada.place(x=50, y=230)

        self.entry_morada = ttk.Entry(self.janela, width=40)
        self.entry_morada.place(x=150, y=230)

        #botoes
        self.botao_add = ttk.Button(self.janela, width=10, text="Adicionar", command=self.adicionar_contato)
        self.botao_add.place(x=50, y=300)

        self.botao_editar = ttk.Button(self.janela, width=10, text="Editar", command=self.editar_contatos)
        self.botao_editar.place(x=200, y=300)

        self.botao_remover = ttk.Button(self.janela, width=10, text="Remover", command=self.remover_contatos)
        self.botao_remover.place(x=350, y=300)

        self.botao_limpar = ttk.Button(self.janela, width=10, text="Limpar", command=self.limpar_contatos)
        self.botao_limpar.place(x=500, y=300)

        self.botao_remover = ttk.Button(self.janela, width=10, text="Favoritar", command=self.favoritar_contatos)
        self.botao_remover.place(x=650, y=300)
        

        estilo = ttk.Style()
        estilo.configure("Treeview", rowheight=35, font=("Helvetica", 12))  # altera a altura das linhas
        estilo.configure("Treeview.Heading", font=("Helvetica", 14, "bold"), foreground="#316C9C")

        #tree
        self.tree = ttk.Treeview(
            self.janela,
            columns=("nome", "telefone", "email", "morada"),
            show="headings",
       
        )
        self.tree.place(x=0, y=380, width=800, height=900)

        self.tree.heading("nome", text="Nome Completo")
        self.tree.heading("telefone", text="Telefone")
        self.tree.heading("email", text="Email")
        self.tree.heading("morada", text="Morada")

        self.tree.column("nome", width=150, anchor="center")
        self.tree.column("telefone", width=120, anchor="center")
        self.tree.column("email", width=180, anchor="center")
        self.tree.column("morada", width=150, anchor="center")

        self.tree.bind("<<TreeviewSelect>>", self.selecionar_contatos)
        self.tree.bind("<Delete>", self.remover_contatos)
        self.tree.bind("<Control-n>", self.adicionar_contato)

        self.carregar_contatos()

    # FUNÇOES
    def carregar_contatos(self):
        ctt = self.db.obter_contatos()
        for nome, telefone, email, morada, concluido in ctt:
            if concluido == 1:
                nome = f"★ {nome}"
            self.tree.insert("", "end", values=(nome, telefone, email, morada))

    def atualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        contatos = self.db.obter_contatos()
        for nome, telefone, email, morada, favorito in contatos:
            if favorito == 1:
                nome = f"★ {nome}"
            self.tree.insert("", "end", values=(nome, telefone, email, morada))


    def adicionar_contato(self):
        nome = self.entry_nome.get() 
        telefone = self.entry_telefone.get() 
        email = self.entry_email.get() 
        morada = self.entry_morada.get()

        if not nome or not telefone or not email or not morada:
            messagebox.showwarning("Aviso!", "Preencha os campos para adicionar um contato!")
            return
        
        contato_existentes = self.db.obter_contatos()
        for c in contato_existentes:
            if c[0] == nome:
                messagebox.showwarning("Aviso!", "Já existe um contato com este nome!")
                return
        
        self.db.adicionar(nome, telefone, email, morada)
        self.tree.insert("", "end", values=(nome, telefone, email, morada)) 
        self.limpar_contatos()
    
    def selecionar_contatos(self, event):
        selecionado = self.tree.selection()
        if not selecionado:
            return
        item = selecionado[0]
        valores = self.tree.item(item, "values")
        self.contato_selecionado = valores[0]

        self.entry_nome.delete(0, "end")
        self.entry_telefone.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_morada.delete(0, "end")

        self.entry_nome.insert(0,valores[0])
        self.entry_telefone.insert("end", valores[1])
        self.entry_email.insert(0, valores[2])
        self.entry_morada.insert(0, valores[3])

    def editar_contatos(self):
        nome_novo = self.entry_nome.get() 
        telefone_novo = self.entry_telefone.get() 
        email_novo = self.entry_email.get() 
        morada_novo = self.entry_morada.get()

        if nome_novo or telefone_novo or email_novo or morada_novo =="":
            messagebox.showwarning("Aviso", "Os campos estão vazios! Preencha-os para editar.")  
            return
        
        self.db.editar(self.contato_selecionado, nome_novo, telefone_novo, email_novo, morada_novo)
        item = self.tree.selection()[0]
        self.tree.item(item, values=(nome_novo, telefone_novo, email_novo, morada_novo))
        
        self.entry_nome.delete(0, "end")
        self.entry_telefone.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_morada.delete(0, "end")

    def remover_contatos(self, event=None):
        selecionados = self.tree.selection()
        if not selecionados:
            messagebox.showwarning("Aviso", "Selecione um contato para remover.")
            return
        item = selecionados[0]
        valores = self.tree.item(item, "values")
        nome = valores[0].replace("★ ", "") 
        self.db.remover(nome)
        self.tree.delete(item)
        self.limpar_contatos()

    def limpar_contatos(self):
        self.entry_nome.delete(0, "end")
        self.entry_telefone.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_morada.delete(0, "end")

    def favoritar_contatos(self):
        item = self.tree.selection()
        if not item:
            return

        item = item[0]
        valores = self.tree.item(item, "values")
        nome = valores[0].replace("★ ", "")  # limpa o nome antes de usar no BD

        favorito_atual = self.db.obter_favorito(nome)
        novo_valor = 0 if favorito_atual else 1
        self.db.favoritar(nome, novo_valor)

        if novo_valor == 1:
            self.tree.item(item, values=(f"★ {nome}", valores[1], valores[2], valores[3]))
        else:
            self.tree.item(item, values=(nome, valores[1], valores[2], valores[3]))

        self.atualizar_lista()
        
    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    app = AppPrincipal()
    app.run()
