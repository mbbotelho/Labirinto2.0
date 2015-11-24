__author__ = 'Douglas'
import pygame,random
pygame.init()

class ControleInimigo:
    def __init__(self):

        self.speed_inimigo = 3

    def controla_direcao(self,labirinto):



        i=0
        while i < len(labirinto.lst_inimigos):

            if labirinto.lst_inimigos[i].direcao==0:
                dy=labirinto.lst_inimigos[i].rect_inimigo[1]
                labirinto.lst_inimigos[i].rect_inimigo[1]-=self.speed_inimigo
                for bloco in labirinto.lst_blocos[:]:
                    if labirinto.lst_inimigos[i].rect_inimigo.colliderect(bloco) or labirinto.lst_inimigos[i].rect_inimigo.colliderect(labirinto.saida):
                        labirinto.lst_inimigos[i].rect_inimigo[1]=dy
                        labirinto.lst_inimigos[i].direcao=random.randint(0,3)

                j=0
                nao_colidir=True

                while j < len(labirinto.lst_tiros) and nao_colidir:
                    if labirinto.lst_inimigos[i].rect_inimigo.colliderect(labirinto.lst_tiros[j]):
                        del labirinto.lst_inimigos[i]
                        del labirinto.lst_tiros[j]
                        del labirinto.lst_direcao_tiro[j]
                        nao_colidir=False
                    j+=1
                if nao_colidir:
                    i+=1

            elif labirinto.lst_inimigos[i].direcao==1:
                dy=labirinto.lst_inimigos[i].rect_inimigo[1]
                labirinto.lst_inimigos[i].rect_inimigo[1]+=self.speed_inimigo
                for bloco in labirinto.lst_blocos[:]:
                    if labirinto.lst_inimigos[i].rect_inimigo.colliderect(bloco) or labirinto.lst_inimigos[i].rect_inimigo.colliderect(labirinto.saida):
                        labirinto.lst_inimigos[i].rect_inimigo[1]=dy
                        labirinto.lst_inimigos[i].direcao=random.randint(0,3)
                j=0
                nao_colidir=True

                while j < len(labirinto.lst_tiros) and nao_colidir:
                    if labirinto.lst_inimigos[i].rect_inimigo.colliderect(labirinto.lst_tiros[j]):
                        del labirinto.lst_inimigos[i]
                        del labirinto.lst_tiros[j]
                        del labirinto.lst_direcao_tiro[j]
                        nao_colidir=False
                    j+=1
                if nao_colidir:
                    i+=1

            elif labirinto.lst_inimigos[i].direcao==2:
                dx=labirinto.lst_inimigos[i].rect_inimigo[0]
                labirinto.lst_inimigos[i].rect_inimigo[0]-=self.speed_inimigo
                for bloco in labirinto.lst_blocos[:]:
                    if labirinto.lst_inimigos[i].rect_inimigo.colliderect(bloco) or labirinto.lst_inimigos[i].rect_inimigo.colliderect(labirinto.saida):
                        labirinto.lst_inimigos[i].rect_inimigo[0]=dx
                        labirinto.lst_inimigos[i].direcao=random.randint(0,3)
                j=0
                nao_colidir=True

                while j < len(labirinto.lst_tiros) and nao_colidir:
                    if labirinto.lst_inimigos[i].rect_inimigo.colliderect(labirinto.lst_tiros[j]):
                        del labirinto.lst_inimigos[i]
                        del labirinto.lst_tiros[j]
                        del labirinto.lst_direcao_tiro[j]
                        nao_colidir=False
                    j+=1
                if nao_colidir:
                    i+=1

            elif labirinto.lst_inimigos[i].direcao==3:
                dx=labirinto.lst_inimigos[i].rect_inimigo[0]
                labirinto.lst_inimigos[i].rect_inimigo[0]+=self.speed_inimigo
                for bloco in labirinto.lst_blocos[:]:
                    if labirinto.lst_inimigos[i].rect_inimigo.colliderect(bloco) or labirinto.lst_inimigos[i].rect_inimigo.colliderect(labirinto.saida):
                        labirinto.lst_inimigos[i].rect_inimigo[0]=dx
                        labirinto.lst_inimigos[i].direcao=random.randint(0,3)
                j=0
                nao_colidir=True

                while j < len(labirinto.lst_tiros) and nao_colidir:
                    if labirinto.lst_inimigos[i].rect_inimigo.colliderect(labirinto.lst_tiros[j]):
                        del labirinto.lst_inimigos[i]
                        del labirinto.lst_tiros[j]
                        del labirinto.lst_direcao_tiro[j]
                        nao_colidir=False
                    j+=1
                if nao_colidir:
                    i+=1
