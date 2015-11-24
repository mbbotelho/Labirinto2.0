__author__ = 'Michelle'

from Fabrica import *

class FabricaInimigoVermelho(Fabrica):

    def carrega_imagem(self):
        return "vermelho"

    def adiciona_pontuacao(self):
       return 4

    def adiciona_sangue(self):
        return 3
