__author__ = 'Michelle'

from BuilderAbstrata import *
from FabricaInimigoRosa import *

class FabricaInimigoRosaBuilder(BuilderAbstrata):
    def __init__(self):
        BuilderAbstrata.__init__(self, FabricaInimigoRosa())