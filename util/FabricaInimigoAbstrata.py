__author__ = 'Michelle'
from util.Fabrica import *

class FabricaInimigoAbstrata(Fabrica):



    def carrega_imagem(self):
        Fabrica.carrega_imagem(self)

    def adiciona_sangue(self):
        Fabrica.adiciona_sangue(self)

    def adiciona_pontuacao(self):
        Fabrica.adiciona_pontuacao(self)

