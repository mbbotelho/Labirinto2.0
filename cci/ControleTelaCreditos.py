from ControleTeclado import *

class ControleTelaCreditos:
    def __init__(self):
                                        #Back   #Voltar   #Quit    #Contorno
        self.posicao_imagens_creditos = [[0,0],[200,500],[310,500],[200,500]]
        self.teclado=ControleTeclado()

    def controla_creditos(self,opcao):

        self.opcao=opcao
        self.esquerda,self.direita,self.esc,self.espaco=2,3,4,6
        self.voltar,self.quit,self.contorno=1,2,3
        self.largura,self.altura=0,1
        self.velocidade_contorno_largura=110
        self.teclado.captura_evento()

        if self.teclado.teclas[self.direita] and (self.posicao_imagens_creditos[self.contorno][self.altura] == self.posicao_imagens_creditos[self.voltar][self.altura] and self.posicao_imagens_creditos[self.contorno][self.largura] < self.posicao_imagens_creditos[self.quit][self.largura]):
            self.posicao_imagens_creditos[self.contorno][self.largura]+=self.velocidade_contorno_largura

        elif self.teclado.teclas[self.esquerda] and (self.posicao_imagens_creditos[self.contorno][self.altura] == self.posicao_imagens_creditos[self.voltar][self.altura] and self.posicao_imagens_creditos[self.contorno][self.largura] > self.posicao_imagens_creditos[self.voltar][self.largura]):
            self.posicao_imagens_creditos[self.contorno][self.largura]-=self.velocidade_contorno_largura

        elif self.teclado.teclas[self.espaco]:
            if self.posicao_imagens_creditos[self.contorno][self.altura]==self.posicao_imagens_creditos[self.voltar][self.altura] and self.posicao_imagens_creditos[self.contorno][self.largura]==self.posicao_imagens_creditos[self.voltar][self.largura]:
                self.opcao=3
                return self.opcao

            elif self.posicao_imagens_creditos[self.contorno][self.altura]==self.posicao_imagens_creditos[self.quit][self.altura] and self.posicao_imagens_creditos[self.contorno][self.largura]==self.posicao_imagens_creditos[self.quit][self.largura]:
                pygame.quit()
                sys.exit()


