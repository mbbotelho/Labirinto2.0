import pygame,random

class Player:

    def __init__(self,lst_posicao_possivel,sangue,pontuacao):
        self.direcao=0
        self.sangue=sangue
        self.pontucao=pontuacao
        lst_sorteada=lst_posicao_possivel[random.randint(0,len(lst_posicao_possivel)-1)]
        self.rect_player = pygame.Rect(lst_sorteada[0],lst_sorteada[1],16,28)