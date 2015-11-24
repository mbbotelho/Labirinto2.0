import pygame,sys,os

class CriarJanela:
    def __init__(self,tupla_altura_largura,string_nome_janela):
        if sys.platform == 'win32' or sys.platform == 'win64':
            os.environ['SDL_VIDEO_CENTERED'] = '1' # comando para iniciar a janela na posicao central da tela
        self.width,self.height = tupla_altura_largura[0],tupla_altura_largura[1]
        self.screen = pygame.display.set_mode((self.width,self.height))  #,RESIZABLE  para add o botao redimen
        pygame.display.set_caption(string_nome_janela)
