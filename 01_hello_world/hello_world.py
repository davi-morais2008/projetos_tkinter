import tkinter as tk

# Criar janela
janela = tk.Tk()
janela.geometry("800x600+100+50")
janela.configure(bg="#4682B4")
janela.title("Hello World!")
janela.iconbitmap("01_hello_world/java.ico")
janela.resizable(True, True)

# Frame central para organizar tudo
frame_central = tk.Frame(janela, bg=janela["bg"])
frame_central.pack(expand=True)  # Mantém no centro

# Título
label_titulo = tk.Label(frame_central, 
                        text="Hello World", 
                        font=("Arial", 24), 
                        foreground="darkblue",
                        bg=janela["bg"])
label_titulo.pack(pady=10)

# Função de mostrar nome
def mostrar_nome():
    nome_digitado = campo_nome.get()
    label_resultado.config(text=f"Olá, {nome_digitado}!")

# Pergunta ao usuário
label_nome = tk.Label(frame_central,
                      text="Digite seu nome abaixo:",
                      font=("Arial", 24),
                      foreground="darkblue",
                      bg=janela["bg"])
label_nome.pack(pady=10)

# Campo de entrada
campo_nome = tk.Entry(frame_central, font=("Arial", 16))
campo_nome.pack(pady=5)

# Botão
botao_enviar = tk.Button(frame_central, 
                         text="Enviar", 
                         command=mostrar_nome,
                         font=("Arial", 16))
botao_enviar.pack(pady=10)

# Resultado
label_resultado = tk.Label(frame_central, 
                           text="", 
                           font=("Arial", 16),
                           bg=janela["bg"])
label_resultado.pack(pady=10)

janela.mainloop()
