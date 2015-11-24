__author__ = 'Douglas'
from util.CriaBotao import *

class CriaTelaMenu:
    def __init__(self):
        self.jogar_imagem = CriarBotao("jogar").cria_botao() # recebe a imagem do botao jogar
        self.creditos_imagem = CriarBotao("creditos").cria_botao() # recebe a imagem do botao creditos
        self.sair_imagem = CriarBotao("sair").cria_botao() # recebe a imagem do botao sair
        self.record_imagem = CriarBotao("record").cria_botao() # recebe a imagem do cursor
        self.cursor_imagem = CriarBotao("cursor").cria_botao() # recebe a imagem do cursor

        self.file_back=os.path.join("imagens","backpequeno.png") #file recebe o local da imagem que sera utilizada
        self.back_imagem = pygame.image.load(self.file_back) # recebe a imagem do background

    def imprime_tela_menu(self,janela,posicao):

        self.background,self.jogar,self.record,self.creditos,self.sair,self.cursor=0,1,2,3,4,5

        janela.screen.blit(self.back_imagem,posicao[self.background]) # printa o background
        janela.screen.blit(self.jogar_imagem,posicao[self.jogar]) # printar o botao jogar
        janela.screen.blit(self.creditos_imagem,posicao[self.creditos]) # printar o botao creditos
        janela.screen.blit(self.record_imagem,posicao[self.record]) # printar o botao sair
        janela.screen.blit(self.sair_imagem,posicao[self.sair]) # printar o botao sair
        janela.screen.blit(self.cursor_imagem,posicao[self.cursor]) # printar o cursor