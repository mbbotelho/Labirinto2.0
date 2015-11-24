__author__ = 'Douglas'
from util.CriaBotao import *
from util.CriarImagem import *


class CriarTelaLogin():
    def __init__(self):

        self.fonte = pygame.font.SysFont("comicsansms",30)
        self.login_imagem = CriarBotao("login").cria_botao() # recebe a imagem do botao login
        self.senha_imagem = CriarBotao("senha").cria_botao() # recebe a imagem do botao senha
        self.confirmar_imagem = CriarBotao("confirmar").cria_botao() # recebe a imagem do botao confirmar
        self.limpar_imagem = CriarBotao("limpar").cria_botao() # recebe a imagem do limpar
        self.cadastrar_imagem = CriarBotao("cadastrar").cria_botao() # recebe a imagem do cadastrar
        self.campo_imagem = CriarImagem("retanguloBranco",(400,40)).cria_botao() # recebe a imagem do campo para escrita
        self.contorno_imagem = CriarBotao("contorno").cria_botao() # recebe a imagem do cursor

        self.file_back=os.path.join("imagens","backpequeno.png") #file recebe o local da imagem que sera utilizada
        self.back_imagem = pygame.image.load(self.file_back) # recebe a imagem do background

    def imprime_tela_login(self,janela,lista_posicao,lstTexto,erro):

        janela.screen.fill(0) #limpar a tela

        self.lstTexto=lstTexto
        login,senha=0,1

        self.texto_login = self.fonte.render(self.lstTexto[login],1,(0,0,0))
        self.texto_senha = self.fonte.render(self.lstTexto[senha],1,(0,0,0))

        janela.screen.blit(self.back_imagem,lista_posicao[0]) # printa o background
        janela.screen.blit(self.login_imagem,lista_posicao[1]) # printar o botao login
        janela.screen.blit(self.senha_imagem,lista_posicao[2]) # printar o botao senha
        janela.screen.blit(self.confirmar_imagem,lista_posicao[3]) # printar o botao confirmar
        janela.screen.blit(self.limpar_imagem,lista_posicao[4]) # printar o limpar
        janela.screen.blit(self.cadastrar_imagem,lista_posicao[5]) # printar o cadastrar
        janela.screen.blit(self.campo_imagem,lista_posicao[6]) # printar o campo
        janela.screen.blit(self.campo_imagem,lista_posicao[7]) # printar o campo
        janela.screen.blit(self.contorno_imagem,lista_posicao[8]) # printar o cursor
        janela.screen.blit(self.texto_login,lista_posicao[6])
        janela.screen.blit(self.texto_senha,lista_posicao[7])

        if erro:
            self.texto_erro = self.fonte.render("Login ou Senha Errado",1,(0,0,0))
            janela.screen.blit(self.texto_erro,(250,450))

        pygame.display.update()