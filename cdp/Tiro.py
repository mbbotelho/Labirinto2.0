import pygame,random

class Tiro:

    def criar_tiro(self,tupla_posicao):

        self.tiro = pygame.Rect(tupla_posicao[0],tupla_posicao[1],5,5)

        return self.tiro

