import pygame,random

class Inimigo:

    def __init__(self,imagem,sangue,pontuacao):
        self.imagem = imagem
        self.direcao=0
        self.sangue=sangue
        self.pontucao=pontuacao

    def cria_rect(self,lst_posicao_possivel):
        lst_sorteada=lst_posicao_possivel[random.randint(0,len(lst_posicao_possivel)-1)]
        self.rect_inimigo = pygame.Rect(lst_sorteada[0],lst_sorteada[1],16,28)