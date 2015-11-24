from ControleTeclado import *

class ControleTelaDerrota:
    def __init__(self):
                                        #Back   #Jogar   #Quit    #Contorno
        self.posicao_imagens_derrota = [[0,0],[400,500],[510,500],[400,500]]
        self.teclado=ControleTeclado()

    def controla_derrota(self,opcao):

        self.opcao=opcao
        self.esquerda,self.direita,self.esc,self.espaco=2,3,4,6
        self.jogar,self.quit,self.contorno=1,2,3
        self.largura,self.altura=0,1
        self.velocidade_contorno_largura=110
        self.teclado.captura_evento()

        if self.teclado.teclas[self.direita] and (self.posicao_imagens_derrota[self.contorno][self.altura] == self.posicao_imagens_derrota[self.jogar][self.altura] and self.posicao_imagens_derrota[self.contorno][self.largura] < self.posicao_imagens_derrota[self.quit][self.largura]):
            self.posicao_imagens_derrota[self.contorno][self.largura]+=self.velocidade_contorno_largura

        elif self.teclado.teclas[self.esquerda] and (self.posicao_imagens_derrota[self.contorno][self.altura] == self.posicao_imagens_derrota[self.jogar][self.altura] and self.posicao_imagens_derrota[self.contorno][self.largura] > self.posicao_imagens_derrota[self.jogar][self.largura]):
            self.posicao_imagens_derrota[self.contorno][self.largura]-=self.velocidade_contorno_largura

        elif self.teclado.teclas[self.espaco]:
            if self.posicao_imagens_derrota[self.contorno][self.altura]==self.posicao_imagens_derrota[self.jogar][self.altura] and self.posicao_imagens_derrota[self.contorno][self.largura]==self.posicao_imagens_derrota[self.jogar][self.largura]:
                self.opcao=3
                return self.opcao

            elif self.posicao_imagens_derrota[self.contorno][self.altura]==self.posicao_imagens_derrota[self.quit][self.altura] and self.posicao_imagens_derrota[self.contorno][self.largura]==self.posicao_imagens_derrota[self.quit][self.largura]:
                pygame.quit()
                sys.exit()

