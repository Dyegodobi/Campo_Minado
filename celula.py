from tkinter import Button, Label
import random
import configurações
import ctypes
import sys

class Celula:
    all = []
    contador_celulas = configurações.Contador_Posicoes
    contador_etiqueta = None
    def __init__(self, x , y , isso_bomba = False):
        self.isso_bomba = isso_bomba
        self.isso_aberto = False
        self.isso_talvez_bomba = False
        self.forma_botao = None
        self.x = x
        self.y = y

        # adciona o objeto chamando a Celula lista
        Celula.all.append(self)

    def criar_botao(self, posição):
        botao = Button(
            posição,
            width = 12,
            height = 4,
        )
        botao.bind('<Button-1>',self.botao_esquerdo)
        botao.bind('<Button-3>',self.botao_direito)
        self.forma_botao = botao

    @staticmethod
    def area_segura_inicial(posição):
        etiqueta = Label(
            posição,
            bg = 'black',
            fg = 'white',
            text=f"Locais faltando:{Celula.contador_celulas}",
            width=12,
            height=4,
            font = ("",30)
        )
        Celula.contador_etiqueta = etiqueta
    
    def botao_esquerdo(self, evento):
        if self.isso_bomba:
            self.mostre_bomba()
        else:
            if self.posicoes_escondidas_comprimentobombas == 0:
                for posicao_objetiva in self.posicoes_escondidas:
                    posicao_objetiva.mostre_posicao()
            self.mostre_posicao()

            if Celula.contador_celulas == configurações.Minas:
                ctypes.windll.user32.MessageBoxW(0, "Venceu!!!" , "Perdeu" , 0)


        self.forma_botao.unbind('<Button-1>')
        self.forma_botao.unbind('<Button-3>')

    def assume_posicao(self, x,y):
        for celula in Celula.all:
            if celula.x == x and celula.y == y:
                return celula

    @property
    def posicoes_escondidas(self):
        celulas = [
            self.assume_posicao(self.x - 1, self.y - 1),
            self.assume_posicao(self.x - 1, self.y),
            self.assume_posicao(self.x - 1, self.y + 1),
            self.assume_posicao(self.x, self.y - 1),
            self.assume_posicao(self.x + 1, self.y - 1),
            self.assume_posicao(self.x + 1, self.y),
            self.assume_posicao(self.x + 1, self.y + 1),
            self.assume_posicao(self.x, self.y + 1),
        ]
        
        celulas = [celula for celula in celulas if celula is not None]
        return celulas
    
    @property
    def posicoes_escondidas_comprimentobombas(self):
        contador = 0
        for celula in self.posicoes_escondidas:
            if celula.isso_bomba:
                contador += 1

        return contador

    def mostre_posicao(self):
        if not self.isso_aberto:
            Celula.contador_celulas -= 1
            self.forma_botao.configure(text=self.posicoes_escondidas_comprimentobombas)
            if Celula.contador_etiqueta:
                Celula.contador_etiqueta.configure(
                    text=f"Posições:{Celula.contador_celulas}"
                )
            self.forma_botao.configure(
                bg = 'SystemButtonFace'
            )

        self.isso_aberto = True

    def mostre_bomba(self):
        self.forma_botao.configure(bg = 'red'),
        ctypes.windll.user32.MessageBoxW(0, "!!!Boom!!!" , "Perdeu" , 0)
        sys.exit()

    def botao_direito(self, evento):
        if not self.isso_talvez_bomba:
            self.forma_botao.configure(
                bg = "orange"
            )
            self.isso_talvez_bomba = True
        else:
            self.forma_botao.configure(
                bg = 'SystemButtonFace'
            )

    @staticmethod
    def bombas_aleatórias():
        posicoes_escolhidas = random.sample(
            Celula.all, configurações.Minas
        )
        for posicoes_escolhida in posicoes_escolhidas:
            posicoes_escolhida.isso_bomba = True


    def __repr__(self):
        return f"Celula({self.x},{self.y})"