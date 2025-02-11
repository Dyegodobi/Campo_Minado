from tkinter import *
import configurações
import utilidades
from celula import Celula
import random

base = Tk()
base.configure(bg="black")
base.geometry(f'{configurações.Largura}x{configurações.Altura}')
base.title("Campo Minado")
base.resizable(False,False)

area_cima = Frame(
    base,
    bg = "black",
    width = configurações.Largura,
    height = utilidades.altura_porcentagem(25)
    )
area_cima.place(x=0, y=0)

titulo_jogo = Label(
    area_cima,
    bg = 'black',
    fg = 'white',
    text = "Campo Minado",
    font = ('',48)
)

titulo_jogo.place(
    x = utilidades.largura_porcentagem(25), y = 0
)

area_esquerda = Frame(
    base,
    bg = "black",
    width = utilidades.largura_porcentagem(25),
    height = utilidades.altura_porcentagem(75)
)
area_esquerda.place(
    x=utilidades.largura_porcentagem(0),
    y=utilidades.altura_porcentagem(25),
    )

area_central = Frame(
    base,
    bg = "black",
    width = utilidades.largura_porcentagem(75),
    height = utilidades.altura_porcentagem(75)
)
area_central.place(
    x=utilidades.largura_porcentagem(25),
    y=utilidades.altura_porcentagem(25),
)

for x in range(configurações.Tam_Grade):
    for y in range(configurações.Tam_Grade):
        c = Celula(x, y)
        c.criar_botao(area_central)
        c.forma_botao.grid(
            column = x, row = y
        )

Celula.area_segura_inicial(area_esquerda)
Celula.contador_etiqueta.place(
    x=0,y=0
    )

Celula.bombas_aleatórias()


base.mainloop()