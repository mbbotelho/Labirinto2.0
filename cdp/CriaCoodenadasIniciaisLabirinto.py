from CriarLabirinto import *
from Inimigo import *
from Labirinto import *
from Player import *
from util.FabricaInimigo import *
import pygame,random


class CoordenadasObjetosLabirinto:

    def __init__(self,largura,altura):

        self.cria_labirinto=CriarLabirinto(largura,altura)
        self.lista_coodernadas_labirinto=self.cria_labirinto.desenha_labirinto(0,0)
        self.lista_inimigos=[]
        self.fabrica_inimigo=FabricaInimigo()


    def objetos(self,qtd_inimigos):

        blocos=self.lista_coodernadas_labirinto[0]
        gramas=self.lista_coodernadas_labirinto[1]
        player = Player(self.lista_coodernadas_labirinto[1],5,5) # paralelepipedo do tamanho do player
        saida = pygame.Rect(self.lista_coodernadas_labirinto[3][0],self.lista_coodernadas_labirinto[3][1],30,30) #localizacao saida
        i=0
        for i in range(0,qtd_inimigos):
            inimigo=self.fabrica_inimigo.criar_inimigo()
            inimigo.cria_rect(gramas)
            self.lista_inimigos.append(inimigo)

        labirinto=Labirinto(player,gramas,blocos,saida,self.lista_inimigos)

        return labirinto