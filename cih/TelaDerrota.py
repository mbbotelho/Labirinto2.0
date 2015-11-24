__author__ = 'Douglas'
from util.CriaBotao import *
from util.CriarImagem import *

class TelaDerrota:
    def __init__(self):

        self.jogar_imagem = CriarBotao("jogar").cria_botao() # recebe a imagem do botao voltar
        self.quit_imagem = CriarBotao("quit").cria_botao() # recebe a imagem do botao sair
        self.contorno_imagem = CriarBotao("contorno").cria_botao() # recebe a imagem do cursor
        self.creditos_imagem = CriarImagem("backderrota",(632,632)).cria_botao() # file recebe o local da imagem que sera utilizada

    def imprime_tela_derrota(self,janela,lista_posicao):

        self.background,self.jogar,self.quit,self.contorno=0,1,2,3

        janela.screen.blit(self.creditos_imagem,lista_posicao[self.background]) # printa o background
        janela.screen.blit(self.jogar_imagem,lista_posicao[self.jogar]) # printa o menu
        janela.screen.blit(self.quit_imagem,lista_posicao[self.quit]) # printar o botao sair
        janela.screen.blit(self.contorno_imagem,lista_posicao[self.contorno]) # printar o cursor