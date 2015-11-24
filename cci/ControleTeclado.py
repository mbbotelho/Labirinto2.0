__author__ = 'Douglas'

import pygame,sys
pygame.init()


class ControleTeclado:

    def __init__(self):

                       #cima  #baixo #esqu  #dire  #esc   #C  #espaco #String
        self.teclas = [False, False, False, False, False, False,False,""]  # lista com as teclas setadas por padrao como falso

    def captura_evento(self):

        self.CIMA,self.BAIXO,self.ESQUERDA,self.DIREITA,self.ESC,self.C,self.ESPACO,self.CHARACTER=0,1,2,3,4,5,6,7

        for event in pygame.event.get(): # para cada evento possivel (o pygame verifica todas a interrupcoes possiveis)

            if event.type == pygame.QUIT: # verifica qual o tipo de evento
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN: # se evento for do tipo tecla pressionada
                if event.key == pygame.K_UP:
                    self.teclas[self.CIMA] = True
                if event.key == pygame.K_DOWN:
                    self.teclas[self.BAIXO] = True
                if event.key == pygame.K_LEFT:
                    self.teclas[self.ESQUERDA] = True
                if event.key == pygame.K_RIGHT:
                    self.teclas[self.DIREITA] = True
                if event.key == pygame.K_ESCAPE:
                    self.teclas[self.ESC] = True
                if event.key == pygame.K_c:
                    self.teclas[self.C] = True
                if event.key == pygame.K_SPACE:
                    self.teclas[self.ESPACO] = True
                if (event.key >= 97 and event.key <= 122) or (event.key >= 48 and event.key <= 57) or (event.key >= 64 and event.key <= 90) or (event.key == 95) or (event.key == 32) or (event.key == 8):
                        self.teclas[self.CHARACTER] = chr(event.key)

            if event.type == pygame.KEYUP: # se evento for do tipo tecla nao pressionada
                if event.key == pygame.K_UP:
                    self.teclas[self.CIMA] = False
                if event.key == pygame.K_DOWN: # verifica qual a tecla nao pressionada
                    self.teclas[self.BAIXO] = False
                if event.key == pygame.K_LEFT:
                    self.teclas[self.ESQUERDA] = False # seta na lista de teclas o estado False
                if event.key == pygame.K_RIGHT:
                    self.teclas[self.DIREITA] = False
                if event.key == pygame.K_ESCAPE:
                    self.teclas[self.ESC] = False
                if event.key == pygame.K_c:
                    self.teclas[self.C] = False
                if event.key == pygame.K_SPACE:
                    self.teclas[self.ESPACO] = False
                if  (event.key >= 97 and event.key <= 122) or (event.key >= 48 and event.key <= 57) or (event.key >= 64 and event.key <= 90) or (event.key == 95) or (event.key == 32) or (event.key == 8):
                        self.teclas[self.CHARACTER] = ""