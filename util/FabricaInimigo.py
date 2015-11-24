__author__ = 'Michelle'
import random
from InimigoFlyweight import *
from Fabricante import *

class FabricaInimigo:
    def __init__(self):

        self.inimigo_flyweight=InimigoFlyweight()
        self.fabricante=Fabricante()

    def criar_inimigo(self):

        nome_inimigo=self.sorteia_inimigo()
        builder=self.inimigo_flyweight.add_builder(nome_inimigo)
        print(builder)
        inimigo=self.fabricante.cria_inimigo(builder)
        print(inimigo.pontucao)
        return inimigo

    def sorteia_inimigo(self):
        tipo_inimigo=["Branco","Rosa","Vermelho"]
        numero_sorteado=random.randint(0,len(tipo_inimigo)-1)
        return tipo_inimigo[numero_sorteado]

