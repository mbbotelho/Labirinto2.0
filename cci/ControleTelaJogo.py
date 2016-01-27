__author__ = 'Douglas'
import pygame

from ControleTeclado import *
from cdp.Tiro import *
from cdp.ControleTiro import *
from cdp.ControleInimigo import *

pygame.init()

class ControleTelaJogo:

    def __init__(self):
        self.speed = 10 # quanto de deslocamento o player recebera (simula a velocidade)
        self.speed_janela=10 #quanto de delocamento a janela recebera
        self.teclado=ControleTeclado()
        self.controla_tiro=ControleTiro()
        self.controle_inimigo=ControleInimigo()

    def controlador_player(self,labirinto,opcao): # funcao que controla o deslocamento do player e suas colisoes
        self.teclado.captura_evento()
        self.opcao=opcao

        if self.teclado.teclas[0]: # verifica se a tecla pressionada foi UP
            labirinto.player.direcao=0

            if labirinto.player.rect_player.top<=80 : # verifica se a parte superior do personagem e maior(mais para baixo) que a posicao Y da tela superior
                labirinto.player.rect_player[1]+=self.speed
                for bloco in labirinto.lst_blocos: # se verdadeiro, todos os objetos sao delocados -Y
                    bloco[1]+=self.speed      # demonstrando uma parte mais superior do labirinto
                labirinto.saida[1]+=self.speed
                for grama in labirinto.lst_gramas:
                    grama[1]+=self.speed
                for inimigo in labirinto.lst_inimigos:
                    inimigo.rect_inimigo[1]+=self.speed
                for tiro in labirinto.lst_tiros:
                    tiro[1]+=self.speed
            if labirinto.player.rect_player.top>=0 : # verifica se a parte superior do personagem e maior(mais para baixo) da tela superior
                dy=labirinto.player.rect_player[1] # guarda a posicao atual do personagem
                labirinto.player.rect_player[1]-=self.speed # adiciona speed a posicao do personagem
                for bloco in labirinto.lst_blocos[:]: # verifica para cada bloco
                    if labirinto.player.rect_player.colliderect(bloco): # se o personagem ira colidir, caso receba a nova posicao
                        labirinto.player.rect_player[1]=dy # se o personagem colidir com algum bloco, personagem recebera a posicao guardada
                for inimig in labirinto.lst_inimigos:
                    if labirinto.player.rect_player.colliderect(inimig.rect_inimigo):
                        self.opcao=10

        elif self.teclado.teclas[1]:
            labirinto.player.direcao=1

            if labirinto.player.rect_player.bottom>=550 : # verifica se a parte inferior do personagem e menor(mais para cima) que a posicao Y da tela superior
                labirinto.player.rect_player[1]-=self.speed
                for bloco in labirinto.lst_blocos: # se verdadeiro, todos os objetos sao delocados +Y
                    bloco[1]-=self.speed            # demonstrando uma parte mais inferior do labirinto
                labirinto.saida[1]-=self.speed
                for grama in labirinto.lst_gramas:
                    grama[1]-=self.speed
                for inimigo in labirinto.lst_inimigos:
                    inimigo.rect_inimigo[1]-=self.speed
                for tiro in labirinto.lst_tiros:
                    tiro[1]-=self.speed
            if labirinto.player.rect_player.bottom<=931 :
                dy=labirinto.player.rect_player[1]
                labirinto.player.rect_player[1]+=self.speed
                for bloco in labirinto.lst_blocos[:]:
                    if labirinto.player.rect_player.colliderect(bloco):
                        labirinto.player.rect_player[1]=dy
                for inimig in labirinto.lst_inimigos:
                    if labirinto.player.rect_player.colliderect(inimig.rect_inimigo):
                        self.opcao=10
        elif self.teclado.teclas[2]:
            labirinto.player.direcao=2

            if labirinto.player.rect_player.left<=100 :
                labirinto.player.rect_player[0]+=self.speed
                for bloco in labirinto.lst_blocos:
                    bloco[0]+=self.speed
                labirinto.saida[0]+=self.speed
                for grama in labirinto.lst_gramas:
                    grama[0]+=self.speed
                for inimigo in labirinto.lst_inimigos:
                    inimigo.rect_inimigo[0]+=self.speed
                for tiro in labirinto.lst_tiros:
                    tiro[0]+=self.speed
            if labirinto.player.rect_player.left>=0:
                dy=labirinto.player.rect_player[0]
                labirinto.player.rect_player[0]-=self.speed
                for bloco in labirinto.lst_blocos[:]:
                    if labirinto.player.rect_player.colliderect(bloco):
                        labirinto.player.rect_player[0]=dy
                for inimig in labirinto.lst_inimigos:
                    if labirinto.player.rect_player.colliderect(inimig.rect_inimigo):
                        self.opcao=10

        elif self.teclado.teclas[3]:
            labirinto.player.direcao=3

            if labirinto.player.rect_player.right>=530 : # verifica se a parte inferior do personagem e menor(mais para cima) que a posicao Y da tela superior
                labirinto.player.rect_player[0]-=self.speed
                for bloco in labirinto.lst_blocos: # se verdadeiro, todos os objetos sao delocados +Y
                    bloco[0]-=self.speed            # demonstrando uma parte mais inferior do labirinto
                labirinto.saida[0]-=self.speed
                for grama in labirinto.lst_gramas:
                    grama[0]-=self.speed
                for inimigo in labirinto.lst_inimigos:
                    inimigo.rect_inimigo[0]-=self.speed
                for tiro in labirinto.lst_tiros:
                    tiro[0]-=self.speed
            if labirinto.player.rect_player.right<=931 :
                dy=labirinto.player.rect_player[0]
                labirinto.player.rect_player[0]+=self.speed
                for bloco in labirinto.lst_blocos[:]:
                    if labirinto.player.rect_player.colliderect(bloco):
                        labirinto.player.rect_player[0]=dy
                for inimig in labirinto.lst_inimigos:
                    if labirinto.player.rect_player.colliderect(inimig.rect_inimigo):
                        self.opcao=10

        # se a tecla 5 (tecla C) pressionada, ele cria um tiro e adiciona um tiro na lista de tiros
        # e uma direcao na lista de direcoes
        if self.teclado.teclas[5]:
            labirinto.lst_tiros.append(Tiro().criar_tiro((labirinto.player.rect_player[0],labirinto.player.rect_player[1])))
            labirinto.lst_direcao_tiro.append(labirinto.player.direcao)

        self.controle_inimigo.controla_direcao(labirinto)
        self.controla_tiro.controla_tiro(labirinto)

        if labirinto.player.rect_player.colliderect(labirinto.saida): # se chegar a saida, altera a opcao do loop principal
            self.opcao=9

        tempo=random.randint(10,100)
        return tempo
