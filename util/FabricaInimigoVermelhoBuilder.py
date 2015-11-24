__author__ = 'Michelle'

from BuilderAbstrata import *
from FabricaInimigoVermelho import *

class FabricaInimigoVermelhoBuilder(BuilderAbstrata):
    def __init__(self):
        BuilderAbstrata.__init__(self, FabricaInimigoVermelho())


