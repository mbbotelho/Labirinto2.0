__author__ = 'Michelle'
from cgd.DaoNivel import *

class AplGerenciaNivel:

    def retorna_id(self,nome_nivel):
        dao_nivel = DaoNivel()
        dao_nivel.iniciar_conexao()
        id_nivel=dao_nivel.retorna_id(nome_nivel)
        dao_nivel.fechar_conexao()
        return id_nivel


