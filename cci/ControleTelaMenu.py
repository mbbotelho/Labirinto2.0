__author__ = 'Douglas'
from ControleTeclado import *
import sys

class ControleTelaMenu:

    def __init__(self):
                                   #Backg #Jogar   #Record  #Credito   #Sair    #Cursor
        self.posicao_imagens_menu=[(0,0),(230,150),(230,250),(230,350),(230,450),[90,150]] # Lista com as posicoes dos botoes
        self.teclado=ControleTeclado()

    def controla_menu(self,opcao):
        self.opcao=opcao
        self.teclado.captura_evento()

        self.cima,self.baixo,self.esquerda,self.direita,self.esc,self.espaco=0,1,2,3,4,6
        self.background,self.jogar,self.record,self.creditos,self.sair,self.cursor=0,1,2,3,4,5
        self.altura=1
        self.velocidade_altura=100

        if self.teclado.teclas[self.cima] and self.posicao_imagens_menu[self.cursor][self.altura] > self.posicao_imagens_menu[self.jogar][self.altura]: # se a tecla up for pressionada e a posicao do cursor for maior que a altura do primeiro icone (no caso o botao jogar)
            self.posicao_imagens_menu[self.cursor][self.altura]-=self.velocidade_altura # a posicao do cursor decrementada em uma quantidade (no caso 100 unidades)

        if self.teclado.teclas[self.baixo] and self.posicao_imagens_menu[self.cursor][self.altura] < self.posicao_imagens_menu[self.sair][self.altura]: # se a tecla down for pressionada e a posicao do cursor for menor que a altura do ultimo icone (no caso o botao sair)
            self.posicao_imagens_menu[self.cursor][self.altura]+=self.velocidade_altura # a posicao do cursor e incrementada em uma quantidade (no caso 100 unidades)

        if self.teclado.teclas[self.espaco]: # se a tecla Space for pressionada
            if self.posicao_imagens_menu[self.cursor][self.altura]==self.posicao_imagens_menu[self.jogar][self.altura]: # se a posicao altura do cursor for a mesma que o botao jogar
                self.opcao=4
                return self.opcao

            elif self.posicao_imagens_menu[self.cursor][self.altura]==self.posicao_imagens_menu[self.record][self.altura]: # se a posicao altura do cursor for a mesma que o botao record
                #self.opcao=7
                #return self.opcao
                 return

            elif self.posicao_imagens_menu[self.cursor][self.altura]==self.posicao_imagens_menu[self.creditos][self.altura]: # se a posicao altura do cursor for a mesma que o botao creditos
                self.opcao=6
                return self.opcao

            elif self.posicao_imagens_menu[self.cursor][self.altura]==self.posicao_imagens_menu[self.sair][self.altura]: # se a posicao altura do cursor for a mesma que o botao sair
                pygame.quit()
                sys.exit()

        if self.teclado.teclas[self.esc]: # se a tecla pressionada for ESC
            pygame.quit()
            sys.exit()

