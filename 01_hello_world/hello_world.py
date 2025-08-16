import tkinter as tk

#CRIAR TELA E DEFINIR FORMATO E POSIÇÃO
janela = tk.Tk()
janela.geometry("1024x768+450+150")

#COR DE FUNDO DA TELA E TITULO
janela.configure(bg="#4682B4")
janela.title("Hello World!")

#FOTO DA JANELA
janela.iconbitmap("01_hello_world/java.ico")




janela.mainloop()
