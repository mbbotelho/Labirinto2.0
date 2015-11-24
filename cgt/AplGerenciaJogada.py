__author__ = 'Michelle'

from cgd.DaoJogada import *


class AplGerenciaJogada:

    def Inserir_jogada(self,jogada):
        dao_jogada = DaoJogada()
        dao_jogada.inciar_conexao()
        dao_jogada.inserir_jogada(jogada)
        dao_jogada.fechar_conexao()


    def  retorna_jogadas_nivel(self,nome_nivel):
        dao_Jogada = DaoJogada()
        dao_Jogada.inciar_conexao()
        lista_jogada= dao_Jogada.retorna_jogadas_nivel(nome_nivel)
        dao_Jogada.fechar_conexao()
        return lista_jogada



