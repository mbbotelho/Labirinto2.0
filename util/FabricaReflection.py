__author__ = 'Michelle'

class FabricaReflection:

    def reflection(self,nome_inimigo):
        contrutor="FabricaInimigo"+nome_inimigo +"Builder"
        nome=[contrutor]
        path = "util." + contrutor
        _temp = __import__(path, fromlist=nome)

        builder= getattr(_temp, contrutor)
        builder = builder()
        return builder


