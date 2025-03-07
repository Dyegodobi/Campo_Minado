#Importando bibliotecas
from tkinter import *
import configurações       #Importa as configurações do jogo(proporção de bombas e tamanho do campo)
import utilidades          #Funções que retornam a largura e altura da janela em porcentagem
from celula import Celula
import random

#Criando a janela principal
base = Tk()
base.configure(bg="black")
base.geometry(f'{configurações.Largura}x{configurações.Altura}')
base.title("Campo Minado")
base.resizable(False,False)

#Criando as áreas da janela;
#Área superior, onde fica o título do jogo;
area_cima = Frame(
    base,
    bg = "black",
    width = configurações.Largura,
    height = utilidades.altura_porcentagem(25)
    )
area_cima.place(x=0, y=0)                                #Posicionamento da área superior, dentro da janela;

titulo_jogo = Label(                          #Configurações do título do jogo;
    area_cima,
    bg = 'black',
    fg = 'white',
    text = "Campo Minado",
    font = ('',48)
)

titulo_jogo.place(                                   #Posicionamento do título do jogo, dentro da área superior;
    x = utilidades.largura_porcentagem(25), y = 0
)
#Área esquerda, onde fica o contador de bombas;
area_esquerda = Frame(
    base,
    bg = "black",
    width = utilidades.largura_porcentagem(25),
    height = utilidades.altura_porcentagem(75)
)
area_esquerda.place(                                #Posicionamento da área esquerda, dentro da janela;
    x=utilidades.largura_porcentagem(0),            
    y=utilidades.altura_porcentagem(25),
    )

#Área central, onde fica o campo minado;
area_central = Frame(
    base,
    bg = "black",
    width = utilidades.largura_porcentagem(75),
    height = utilidades.altura_porcentagem(75)
)
area_central.place(                             #Posicionamento da área central, dentro da janela;
    x=utilidades.largura_porcentagem(25),
    y=utilidades.altura_porcentagem(25),
)

#Criando as células do campo minado;
for x in range(configurações.Tam_Grade):
    for y in range(configurações.Tam_Grade):
        c = Celula(x, y)
        c.criar_botao(area_central)
        c.forma_botao.grid(
            column = x, row = y
        )

#Colocando o contador de bombas na área esquerda;
Celula.area_segura_inicial(area_esquerda)
Celula.contador_etiqueta.place(                     #Posicionamento do contador de bombas, dentro da área esquerda;
    x=0,y=0
    )



base.mainloop()                             #Inicia o loop que mantém a janela aberta para o usuário interagir;