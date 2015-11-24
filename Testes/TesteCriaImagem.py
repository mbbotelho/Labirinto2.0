import pygame,os

class CriarImagem:
    def cria_imagem(self,nome):
        try:
            self.tiponome=nome+".png" # compilar a String nome com o tipo de imagem .png
            return self.tiponome
        except Exception:
            print("nome de imagem invalida")

    def cria_botao(self,nome,tupla_tamanho):
        try:
            self.tiponome=nome+".png" # compilar a String nome com o tipo de imagem .png
            return self.tiponome
        except Exception:
            print("nome de imagem invalida")