#!/usr/bin/env python
from Testes.TesteTecladoDirecional import *
from Testes.TesteCriaImagem import *
from cci.ControleTelaCadastro import *
from cdp.Inimigo import *
from cdp.Jogada import *
from cdp.Tiro import *

import unittest

class TestTecla(unittest.TestCase):

    def teste_tecla_cima(self):
        self.assertEqual(TesteTeclado().rodaTeclado(),True)
    def teste_tecla_baixo(self):
        self.assertEqual(TesteTeclado().rodaTeclado_baixo(),False)
    def teste_tecla_esquerda(self):
        self.assertEqual(TesteTeclado().rodaTeclado_esquerda(),True)
    def teste_tecla_direita(self):
        self.assertEqual(TesteTeclado().rodaTeclado_direita(),True)

class TestCriaImagem(unittest.TestCase):

    def teste_cria_imagem(self):
        self.assertEqual(CriarImagem().cria_imagem("inimigo"),"inimigo.png")
    def teste_cria_botao(self):
        self.assertEqual(CriarImagem().cria_botao("inimigo",(10,10)),"inimigo.png")


class TestaCadastro(unittest.TestCase):

    lista_teste=[(0,0),(50,150),(50,200),(50,250),(50,300),(50,350),(250,450),(360,450),(470,450),(200,150),(200,200),(200,250),(200,300),(200,350),[50,150]]
    def testa_cadastro(self):
        self.assertEqual(ControleCadastro().posicao_imagens_cadastro,self.lista_teste)

class TestaCriaInimigo(unittest.TestCase):

    posicao_possivel=[(0,0),(50,150),(50,200)]
    pontuacao=10
    sangue=15
    inimigo=Inimigo("inimigo",sangue,pontuacao)
    inimigo.cria_rect(posicao_possivel)

    def testa_cria_inimigo_pontuacao(self):
        self.assertEqual(self.inimigo.pontucao,10)
    def testa_cria_inimigo_sangue(self):
        self.assertEqual(self.inimigo.sangue,15)

class TestaCriaJogada(unittest.TestCase):

    pessoa="Douglas"
    nivel=10
    tempo=15
    jogada=Jogada(pessoa,nivel,tempo)

    def testa_cria_jogada_pessoa(self):
        self.assertEqual(self.jogada.id_pessoa,"Douglas")
    def testa_cria_jogada_tempo(self):
        self.assertEqual(self.jogada.tempo,15)
    def testa_cria_jogada_nivel(self):
        self.assertEqual(self.jogada.id_nivel,10)

class TestaCriaTiro(unittest.TestCase):

    tuple_posicao=(200,150)
    tiro=Tiro().criar_tiro(tuple_posicao)

    def cria_tiro(self):
        self.assertEqual(self.tiro[0],200)

if __name__ == '__main__':
    unittest.main()