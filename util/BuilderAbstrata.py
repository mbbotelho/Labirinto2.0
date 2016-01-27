__author__ = 'Michelle'
from cdp.Inimigo import *
from util.Builder import *

class BuilderAbstrata(Builder):

    def __init__(self,fabrica):
        self.fabrica = fabrica

    def preparar_imagem(self):
        self.imagem=self.fabrica.carrega_imagem()
        print(self.imagem)


    def prepara_pontuacao(self):
        self.pontuacao=self.fabrica.adiciona_pontuacao()
        print(self.pontuacao)

    def prepara_sangue(self):
        self.sangue=self.fabrica.adiciona_sangue()
        print(self.sangue)


    def prepara_inimigo(self):
        self.inimigo=Inimigo(self.imagem,self.sangue,self.pontuacao)
        return self.inimigo




