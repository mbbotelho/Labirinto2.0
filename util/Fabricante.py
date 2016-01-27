__author__ = 'Michelle'
from Diretor import *
from Builder import *

class Fabricante(Diretor):

    def cria_inimigo(self,builder):
        builder.preparar_imagem()
        builder.prepara_pontuacao()
        builder.prepara_sangue()
        return builder.prepara_inimigo()

