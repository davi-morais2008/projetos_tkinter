import tkinter as tk

#CRIAR TELA E DEFINIR FORMATO E POSIÇÃO
janela = tk.Tk()
janela.geometry("800x600+100+50")

#COR DE FUNDO DA TELA E TITULO
janela.configure(bg="#4682B4")
janela.title("Hello World!")

#FOTO DA JANELA
janela.iconbitmap("01_hello_world/java.ico")

#IMPEDIR QUE O USUÁRIO REDIMENSIONE A JANELA
janela.resizable(True, True)

frame_centro = tk.Frame(janela, bg=janela["bg"])
frame_centro.pack(expand=True)


#COLOCANDO TEXTOS NO JANELA
label_titulo = tk.Label(janela, 
                        text="Hello World", 
                        font=("Arial", 24), 
                        foreground="darkblue",
                        bg=janela["bg"],
                        )

label_titulo.pack(pady=10)

#FUNÇÃO DE MOSTRAR NOME
def mostrar_nome():
    nome_digitado = campo_nome.get()
    label_resultado.config(text=f"Olá, {nome_digitado}!")

#PERGUNTANDO NOME AO USUÁRIO
label_nome = tk.Label(text="Digite seu nome abaixo:",
                      font=("Arial", 24),
                      foreground="darkblue",
                      bg=janela["bg"])
label_nome.pack(pady=10)

#CAMPO DE DIGITAR O NOME
campo_nome = tk.Entry(janela)
campo_nome.pack(pady=10)

#BOTAO DE ENVIAR O NOME
botao_enviar = tk.Button(janela, 
                         text="Enviar", 
                         command=mostrar_nome,
                         font=("Arial", 16))
botao_enviar.pack(pady=5)

#MOSTRAR O TEXTO COM O NOME DIGITADO
label_resultado = tk.Label(janela, 
                           text="", 
                           bg=janela["bg"])
label_resultado.pack()


janela.mainloop()