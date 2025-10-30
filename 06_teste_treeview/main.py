import ttkbootstrap as ttk

def apagar_item():
   item_selecionado = treeview.selection()
   treeview.delete(item_selecionado)

display = ttk.Window(themename="darkly")
display.geometry("800x600+100+50")
treeview = ttk.Treeview(display)
treeview.pack()

treeview["columns"] = ("nome", "idade", "cidade")

treeview.heading("nome", text="Nome Completo")
treeview.heading("idade", text="Idade")
treeview.heading("cidade", text="Cidade")

treeview.column("idade", width=80)

treeview.insert("", "end", values=["Davi", "3", "nigga city"])
treeview.insert("", "end", values=["Rafeel", "23", "Matao"])
treeview.insert("", "end", values=["Levi", "3", "Araraquara"])
treeview.insert("", "end", values=["Miguel", "33", "Araraquara"])


ttk.Button(display, text="DELETAR", command=apagar_item).pack()

display.mainloop()