__author__ = 'Michelle'
from AplGerenciarPessoa import *
from AplGerenciaJogada import *

class AplGerenciaRecord :

    def record(self,nome_nivel):
        apl_gerecia_pessoa=AplGerenciarPessoa()
        apl_gerecia_jogada=AplGerenciaJogada()
        lista_record=[]
        lista_jogada=apl_gerecia_jogada.retorna_jogadas_nivel(nome_nivel)
        lista_jogada.sort(key=lambda x: x[2])
        i=0
        if lista_jogada != None:

            while i< 5 and i<len(lista_jogada):
                jogada=list(lista_jogada[i][1:3])
                jogada[0]=apl_gerecia_pessoa.retorna_nome(jogada[0])
                lista_record.append(jogada)

                i=i+1

            return lista_record
        else:
            return lista_jogada







