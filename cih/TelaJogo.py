__author__ = 'Douglas'
from util.CriarImagem import *

class TelaJogo:
    def __init__(self):

        self.player_imagem = CriarImagem("player",(16,28)).cria_botao() # recebe as Componente a serem imprimidas
        self.grama_imagem = CriarImagem("grama",(30,30)).cria_botao()
        self.bloco_imagem = CriarImagem("bloco",(30,30)).cria_botao()
        self.saida_imagem = CriarImagem("saida",(30,30)).cria_botao()
        self.back_imagem = CriarImagem("backJogo",(1080,1080)).cria_botao()
        self.inimigo_branco_imagem = CriarImagem("inimigobranco",(16,28)).cria_botao() # recebe as Componente a serem imprimidas
        self.inimigo_vermelho_imagem = CriarImagem("inimigovermelho",(16,28)).cria_botao() # recebe as Componente a serem imprimidas
        self.inimigo_rosa_imagem = CriarImagem("inimigorosa",(16,28)).cria_botao() # recebe as Componente a serem imprimidas
        self.tiro_imagem = CriarImagem("tiro",(5,5)).cria_botao() # recebe as Componente a serem imprimidas

    def imprime_tela_jogo(self,janela,labirinto):


        janela.screen.blit(self.back_imagem,(0,0)) # printar a tela de fundo (background)

        for grama in labirinto.lst_gramas: # printando as gramas
            janela.screen.blit(self.grama_imagem,grama)

        for bloco in labirinto.lst_blocos: # printando os blocos
            janela.screen.blit(self.bloco_imagem,bloco)

        janela.screen.blit(self.player_imagem,labirinto.player.rect_player) # printar a tela (com player)
        janela.screen.blit(self.saida_imagem,labirinto.saida) # printando a saida
        for inimigo in labirinto.lst_inimigos:
            if inimigo.imagem=="branco":
                janela.screen.blit(self.inimigo_branco_imagem,inimigo.rect_inimigo)
            elif inimigo.imagem=="rosa":
                janela.screen.blit(self.inimigo_rosa_imagem,inimigo.rect_inimigo)
            elif inimigo.imagem=="vermelho":
                janela.screen.blit(self.inimigo_vermelho_imagem,inimigo.rect_inimigo)
        for tiro in labirinto.lst_tiros:
            print("direcao do tiro no print",tiro)
            janela.screen.blit(self.tiro_imagem,tiro)


