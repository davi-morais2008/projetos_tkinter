import tkinter as tk


class Calculadora_imc:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.geometry("800x600+100+50")
        self.label_conta = tk.Label(self.janela, text=f"", font=("Segoe UI", 20), bg="#4e4d54")
        self.label_conta.pack(pady=10)
        self.janela.title("Calculadora IMC")
        self.janela.resizable(True,True)
        self.janela.configure(bg= "#4e4d54")
        
        self.frame_central = tk.Frame(self.janela, bg="#4e4d54")
        self.frame_central.pack(expand=True)


        self.label_titulo = tk.Label(self.frame_central,
                                     text= "Calculadora de IMC",
                                     font=("Segoe UI", 25),
                                     fg="white",
                                     bg="#4e4d54")
        self.label_titulo.pack(pady=10)

        #ENTRADA PESO
        self.label_peso = tk.Label(self.frame_central,
                                     text="Digite seu peso em kg:",
                                     font=("Segoe UI", 15),
                                     fg="white",
                                     bg="#4e4d54")
        self.label_peso.pack(pady=(10))

        #ENTRADA PESO
        self.entry_peso = tk.Entry(self.frame_central,
                                   bg="#fff",
                                   font=("Segoe UI", 10),
                                   width=30)
        self.entry_peso.pack(pady=5)
        
        #TEXTO ALTUA
        self.label_altura = tk.Label(self.frame_central,
                                     text="Digite sua altura em Metros:",
                                     font=("Segoe UI", 15),
                                     fg="white",
                                     bg="#4e4d54")
        self.label_altura.pack(pady=(10))

        #ENTRADA ALTURA
        self.entry_altura = tk.Entry(self.frame_central,
                                   bg="#FFF",
                                   font=("Segoe UI", 10),
                                   width=30)
        self.entry_altura.pack(pady=5)

        self.botao_enviar = tk.Button(self.frame_central,
                                      text="Enviar",
                                      bg="#8a8a8d",
                                      width= 15,
                                      height=2,
                                      command= self.todas_funcoes)
        self.botao_enviar.pack(pady=5)
        
        
        self.botao_retornar = tk.Button(self.frame_central,
                                      text="Retornar",
                                      bg="#8a8a8d",
                                      width= 15,
                                      height=2,
                                      command= self.retornar)

    def calcular(self):
        try:
            valor = float(self.entry_peso.get())
            valor2 = float(self.entry_altura.get())
            conta = valor / (valor2**2)
            if conta < 18.5:
                cor = "red"
                status = "Abaixo Do Peso"

            elif conta >= 18.5 and conta < 24.9:
                cor = "green"
                status = "Peso Normal"

            elif conta >= 25.9 and conta <29.9:
                cor = "orange"
                status = "Pré-Obesidade"

            elif conta >= 30 and conta < 34.9:
                cor = "red"
                status = "Obesidade Grau I"
            
            elif conta >= 34.9 and conta < 39.9:
                cor = "red"
                status = "Obesidade Grau II"

            elif conta > 40:
                cor = "red"
                status = "Obesidade Grau III"
            
            self.label_conta.config(text=f"Seu IMC é: {conta:.2f} - Classificação: {status}", fg=cor)
            self.label_conta.pack(pady=10)

        except ValueError:
            self.label_erro = tk.Label(self.frame_central, text="Erro! Digite um número.", font=("Segoe UI", 20))
            self.label_erro.pack(pady=15)



                
        
    
    def apagar(self):
        self.label_titulo.pack_forget()
        self.label_peso.pack_forget()
        self.entry_peso.pack_forget()
        self.label_altura.pack_forget()
        self.entry_altura.pack_forget()
        self.botao_enviar.pack_forget()
        self.botao_retornar.pack(pady=10)
    
    def retornar(self):
        self.label_conta.pack_forget()
        self.botao_retornar.pack_forget()
        self.label_titulo.pack(pady=10)
        self.label_peso.pack(pady=10)
        self.entry_peso.pack(pady=5)
        self.label_altura.pack(pady=10)
        self.entry_altura.pack(pady=5)
        self.botao_enviar.pack(pady=5)
        

    def todas_funcoes(self):
        self.calcular()
        self.apagar()


    
    def run(self):
        self.janela.mainloop()


if __name__ == "__main__":
    bot = Calculadora_imc()
    bot.run()


