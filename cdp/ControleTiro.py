__author__ = 'Douglas'
import pygame,random
pygame.init()

class ControleTiro:
    def __init__(self):

        self.speed_tiro = 5

    def controla_tiro(self,labirinto):

        i=0
        while i < len(labirinto.lst_tiros):

            if labirinto.lst_direcao_tiro[i]==0:
                labirinto.lst_tiros[i][1]-=self.speed_tiro
                self.tam_lst_blocos=len(labirinto.lst_blocos)
                j=0
                nao_colidir=True
                while j < self.tam_lst_blocos and nao_colidir:
                    if labirinto.lst_tiros[i].colliderect(labirinto.lst_blocos[j]) or labirinto.lst_tiros[i].colliderect(labirinto.saida):
                        del labirinto.lst_tiros[i]
                        del labirinto.lst_direcao_tiro[i]
                        nao_colidir=False
                    j+=1
                if nao_colidir:
                    i+=1

            elif labirinto.lst_direcao_tiro[i]==1:
                labirinto.lst_tiros[i][1]+=self.speed_tiro
                self.tam_lst_blocos=len(labirinto.lst_blocos)
                j=0
                nao_colidir=True
                while j < self.tam_lst_blocos and nao_colidir:
                    if labirinto.lst_tiros[i].colliderect(labirinto.lst_blocos[j]) or labirinto.lst_tiros[i].colliderect(labirinto.saida):
                        del labirinto.lst_tiros[i]
                        del labirinto.lst_direcao_tiro[i]
                        nao_colidir=False
                    j+=1
                if nao_colidir:
                    i+=1

            elif labirinto.lst_direcao_tiro[i]==2:
                labirinto.lst_tiros[i][0]-=self.speed_tiro
                self.tam_lst_blocos=len(labirinto.lst_blocos)
                j=0
                nao_colidir=True
                while j < self.tam_lst_blocos and nao_colidir:
                    if labirinto.lst_tiros[i].colliderect(labirinto.lst_blocos[j]) or labirinto.lst_tiros[i].colliderect(labirinto.saida):
                        del labirinto.lst_tiros[i]
                        del labirinto.lst_direcao_tiro[i]
                        nao_colidir=False
                    j+=1
                if nao_colidir:
                    i+=1

            elif labirinto.lst_direcao_tiro[i]==3:
                labirinto.lst_tiros[i][0]+=self.speed_tiro
                self.tam_lst_blocos=len(labirinto.lst_blocos)
                j=0
                nao_colidir=True
                while j < self.tam_lst_blocos and nao_colidir:
                    if labirinto.lst_tiros[i].colliderect(labirinto.lst_blocos[j]) or labirinto.lst_tiros[i].colliderect(labirinto.saida):
                        del labirinto.lst_tiros[i]
                        del labirinto.lst_direcao_tiro[i]
                        nao_colidir=False
                    j+=1
                if nao_colidir:
                    i+=1

