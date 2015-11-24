import pygame,os

class CriarImagem:
    def __init__(self,nome,tupla_tamanho):
        self.tiponome=nome+".png" # compilar a String nome com o tipo de imagem .png
        self.tamanho=tupla_tamanho # tamanho que desejo os botoes

    def cria_botao(self):
        self.file=os.path.join("imagens",self.tiponome) # file recebe o local da imagem que sera utilizada e o nome da imagem
        self.imagem = pygame.image.load(self.file) # carrega a imagem
        return pygame.transform.scale(self.imagem,self.tamanho) # redimensiona a imagem