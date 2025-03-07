from tkinter import Button, Label
import random
import configurações    # Importa as configurações do jogo(proporção de bombas e tamanho do campo)
import ctypes
import sys

# Área que vai ficar armazenado todas nossas funções, com o objetivo de ser o núcleo da celula.py
cont = 0
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

        # Adciona o objeto chamando a Celula lista
        Celula.all.append(self)

    # Função com o objetivo de criar um icone, nomeado de botão
    def criar_botao(self, posição):
        # Definindo tamanho do botão
        botao = Button(        
            posição,
            width = 12,
            height = 4,
        )
        botao.bind('<Button-1>',self.botao_esquerdo)                # Definindo o botão esquerdo e direito
        botao.bind('<Button-3>',self.botao_direito)
        self.forma_botao = botao

    @staticmethod            # Necessário utilizar o staticmethod, para conseguir incorporar a mecânica do botão esquerdo
    # Tem a função de definir o um texto, que  mostra quantas casas restam para acabar o jogo
    def area_segura_inicial(posição):
        # Estilo da etiqueta
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
        
    # Função que vai definir o clique com o botão esquerdo em algum objeto, além de definir o ponto seguro
    def botao_esquerdo(self, evento):
        global cont
        
        # Definindo cont como 0 para garantir que a primeira casa vai ser segura
        if cont==0:
            Celula.bombas_aleatórias(self)
        if self.isso_bomba:
            self.mostre_bomba()
        else:   
            if self.posicoes_escondidas_comprimentobombas == 0:
                for posicao_objetiva in self.posicoes_escondidas:
                    posicao_objetiva.mostre_posicao()
            self.mostre_posicao()
            #Definindo o que é necessário para vencer o jogo
            if Celula.contador_celulas == configurações.Minas:
                ctypes.windll.user32.MessageBoxW(0, "!!!Venceu!!!" , "Você venceu!" , 0)
        cont+=1

        self.forma_botao.unbind('<Button-1>')
        self.forma_botao.unbind('<Button-3>')

    # Para garantir isso ser visto pelo jogador
    def assume_posicao(self, x,y):
        for celula in Celula.all:
            if celula.x == x and celula.y == y:
                return celula

    @property  # Funciona como uma camuflagem, que é exatamente nosso objetivo
    # Define as pósições para garantir que não vai pra fora da área das bombas, para impedir bugs
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
    # Serve de suporte para a função acima, com intuito de deixar essa camuflagem impossível de ser vista
    def posicoes_escondidas_comprimentobombas(self):
        contador = 0
        for celula in self.posicoes_escondidas:
            if celula.isso_bomba:
                contador += 1

        return contador
        
    # Revela a casa após o clique, deixando claro a derrota ou continuação do jogo
    def mostre_posicao(self):
        if not self.isso_aberto:
            Celula.contador_celulas -= 1
            self.forma_botao.configure(text=self.posicoes_escondidas_comprimentobombas)
            if Celula.contador_etiqueta:
                Celula.contador_etiqueta.configure(
                    text=f"Faltam:{Celula.contador_celulas-configurações.Minas} casas"
                )
            self.forma_botao.configure(
                bg = 'SystemButtonFace'
            )

        self.isso_aberto = True

    # Agora revelamos que é bomba aqui, aparecendo a tela de derrota
    def mostre_bomba(self):
        self.forma_botao.configure(bg = 'red'),
        ctypes.windll.user32.MessageBoxW(0, "!!!Boom!!!" , "Perdeu" , 0)
        sys.exit()

    # Evento do botão direito, que tem como objetivo adiciona uma marcação, para prever onde pode ter bombas
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
            self.isso_talvez_bomba = False

    @staticmethod
    # Função que quando chamada, coloca aleatoriamente as bombas pelo campo minado
    def bombas_aleatórias(self):
        posicoes_escolhidas = random.sample(
            Celula.all, configurações.Minas
        )
        for posicoes_escolhida in posicoes_escolhidas:
            posicoes_escolhida.isso_bomba = True
        self.isso_bomba = False

    def __repr__(self):
        return f"Celula({self.x},{self.y})"
