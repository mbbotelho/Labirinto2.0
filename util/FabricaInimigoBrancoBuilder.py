__author__ = 'Michelle'


from BuilderAbstrata import *
from FabricaInimigoBranco import *

class FabricaInimigoBrancoBuilder(BuilderAbstrata):
    def __init__(self):
        BuilderAbstrata.__init__(self, FabricaInimigoBranco())
