import tkinter as tk
import random

def mover_botao():
    
    nova_posicao_x = random.randint(0, largura_janela - largura_botao)
    nova_posicao_y = random.randint(0, altura_janela - altura_botao)
    
    janela.geometry(f"{largura_janela}x{altura_janela}+{nova_posicao_x}+{nova_posicao_y}")

janela = tk.Tk()
janela.title("Botão Fugitivo")

botao = tk.Button(janela, text="Aperte aqui", command=mover_botao)
botao.pack()

largura_janela = janela.winfo_reqwidth()
altura_janela = janela.winfo_reqheight()
largura_botao = botao.winfo_reqwidth()
altura_botao = botao.winfo_reqheight()

janela.mainloop()
