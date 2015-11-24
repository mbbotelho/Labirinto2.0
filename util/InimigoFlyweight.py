__author__ = 'Michelle'

from FabricaReflection import *

class InimigoFlyweight():
    def __init__(self):
        self.fabrica_reflection=FabricaReflection()
        self.dic_builder={}

    def add_builder(self,nome_inimigo):
        if nome_inimigo not in self.dic_builder.keys():
            self.dic_builder[nome_inimigo] = self.fabrica_reflection.reflection(nome_inimigo)
        return self.dic_builder[nome_inimigo]

