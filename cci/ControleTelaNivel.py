__author__ = 'Douglas'
from ControleTeclado import *

class ControleTelaNivel:
    def __init__(self):
                     #Backg  #Facil   #Medio   #Dificil    #Voltar  #Cursor
        self.posicao_imagens_nivel=[(0,0),(230,150),(230,250),(230,350),(230,450),[90,150]]
        self.teclado=ControleTeclado()

    def controle_tela_nivel(self,opcao):
        print(opcao,"opcao passada para nivel")
        self.opcao=opcao
        print(self.opcao,"self.opcao recebida por nivel")
        self.teclado.captura_evento()
        self.cima,self.baixo,self.esc,self.espaco=0,1,4,6
        self.background,self.facil,self.medio,self.dificil,self.voltar,self.cursor=0,1,2,3,4,5
        self.altura=1
        self.velocidade_altura=100

        if self.teclado.teclas[self.cima]:
            if self.posicao_imagens_nivel[self.cursor][self.altura] > self.posicao_imagens_nivel[self.facil][self.altura]:
                self.posicao_imagens_nivel[self.cursor][self.altura]-=self.velocidade_altura

        elif self.teclado.teclas[self.baixo]:
            if self.posicao_imagens_nivel[self.cursor][self.altura] < self.posicao_imagens_nivel[self.voltar][self.altura]:
                self.posicao_imagens_nivel[self.cursor][self.altura]+=self.velocidade_altura

        elif self.teclado.teclas[self.espaco]:
            if self.posicao_imagens_nivel[self.cursor][self.altura]==self.posicao_imagens_nivel[self.facil][self.altura]:
                self.opcao=9
                return self.opcao

            elif self.posicao_imagens_nivel[self.cursor][self.altura]==self.posicao_imagens_nivel[self.medio][self.altura]:
                self.opcao=10
                return self.opcao

            elif self.posicao_imagens_nivel[self.cursor][self.altura]==self.posicao_imagens_nivel[self.dificil][self.altura]:
                self.opcao=11
                return self.opcao

            elif self.posicao_imagens_nivel[self.cursor][self.altura]==self.posicao_imagens_nivel[self.voltar][self.altura]:
                self.opcao=3
                return self.opcao



