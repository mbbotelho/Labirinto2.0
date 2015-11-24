__author__ = 'Douglas'
from util.CriarImagem import *

class TelaAbertura:
    def __init__(self):

        self.background_abertura_imagem = CriarImagem("abertura",(632,632)).cria_botao() # recebe as Componente a serem imprimidas

    def imprime_tela_abertura(self,janela):

        janela.screen.blit(self.background_abertura_imagem,(0,0)) # printar a tela de fundo (background)