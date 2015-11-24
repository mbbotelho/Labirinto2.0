__author__ = 'Douglas'
from util.CriaBotao import *

class TelaNivel:
    def __init__(self):

        self.facil_imagem = CriarBotao("facil").cria_botao() # recebe a imagem a ser utilizada
        self.medio_imagem = CriarBotao("medio").cria_botao()
        self.dificil_imagem = CriarBotao("dificil").cria_botao()
        self.voltar_imagem = CriarBotao("voltar").cria_botao()
        self.cursor_imagem = CriarBotao("cursor").cria_botao()

        self.back = (0,0) # paralelepipedo do tamanho do botao
        self.file_back=os.path.join("imagens","backpequeno.png") #file recebe o local da imagem que sera utilizada
        self.back_imagem = pygame.image.load(self.file_back)

    def imprime_tela_nivel(self,janela,posicao):

        self.background,self.facil,self.medio,self.dificil,self.voltar,self.cursor=0,1,2,3,4,5

        janela.screen.blit(self.back_imagem,posicao[self.background]) # printar a tela
        janela.screen.blit(self.facil_imagem,posicao[self.facil]) # printar a tela
        janela.screen.blit(self.medio_imagem,posicao[self.medio]) # printar a tela
        janela.screen.blit(self.dificil_imagem,posicao[self.dificil]) # printar a tela
        janela.screen.blit(self.voltar_imagem,posicao[self.voltar]) # printar a tela
        janela.screen.blit(self.cursor_imagem,posicao[self.cursor]) # printar a tela