__author__ = 'Douglas'
from util.CriaBotao import *
from util.CriarImagem import *

class TelaCadastro:
    def __init__(self):
        self.fonte = pygame.font.SysFont("comicsansms",30)
        self.nome_imagem = CriarBotao("nome").cria_botao() # recebe a imagem do botao nome
        self.login_imagem = CriarBotao("login").cria_botao() # recebe a imagem do botao login
        self.senha_imagem = CriarBotao("senha").cria_botao() # recebe a imagem do botao senha
        self.email_imagem = CriarBotao("email").cria_botao() # recebe a imagem do botao email
        self.voltar_imagem = CriarBotao("voltar").cria_botao() # recebe a imagem do botao nome
        self.nascimento_imagem = CriarBotao("dataNascimento").cria_botao() # recebe a imagem do data de nascimento
        self.confirmar_imagem = CriarBotao("confirmar").cria_botao() # recebe a imagem do confirmar
        self.limpar_imagem = CriarBotao("limpar").cria_botao() # recebe a imagem do botao nome
        self.campo_imagem = CriarImagem("retanguloBranco",(400,40)).cria_botao() # recebe a imagem do campo para escrita
        self.contorno_imagem = CriarBotao("contorno").cria_botao() # recebe a imagem do cursor

        self.file_back=os.path.join("imagens","backpequeno.png") #file recebe o local da imagem que sera utilizada
        self.back_imagem = pygame.image.load(self.file_back) # recebe a imagem do background

    def imprime_tela_cadastro(self,janela,lista_posicao,lstTexto,erro):

        self.background,self.nome,self.login,self.senha,self.email,self.dataNascimento,self.confirmar,self.limpar,self.voltar,\
        self.campo1,self.campo2,self.campo3,self.campo4,self.campo5,self.contorno=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14

        self.lstTexto=lstTexto
        nome,login,senha,email,nascimento=0,1,2,3,4
        self.texto_nome = self.fonte.render(self.lstTexto[nome],1,(0,0,0))
        self.texto_login = self.fonte.render(self.lstTexto[login],1,(0,0,0))
        self.texto_senha = self.fonte.render(self.lstTexto[senha],1,(0,0,0))
        self.texto_email = self.fonte.render(self.lstTexto[email],1,(0,0,0))
        self.texto_nascimento = self.fonte.render(self.lstTexto[nascimento],1,(0,0,0))

        janela.screen.blit(self.back_imagem,lista_posicao[self.background]) # printa o background
        janela.screen.blit(self.nome_imagem,lista_posicao[self.nome]) # printar o botao nome
        janela.screen.blit(self.login_imagem,lista_posicao[self.login]) # printar o botao login
        janela.screen.blit(self.senha_imagem,lista_posicao[self.senha]) # printar o botao senha
        janela.screen.blit(self.email_imagem,lista_posicao[self.email]) # printar o botao email
        janela.screen.blit(self.nascimento_imagem,lista_posicao[self.dataNascimento]) # printar o botao nascimento
        janela.screen.blit(self.confirmar_imagem,lista_posicao[self.confirmar]) # printar o botao confirmar
        janela.screen.blit(self.limpar_imagem,lista_posicao[self.limpar]) # printar o limpar
        janela.screen.blit(self.voltar_imagem,lista_posicao[self.voltar]) # printar o botao voltar
        janela.screen.blit(self.campo_imagem,lista_posicao[self.campo1]) # printar o campo
        janela.screen.blit(self.campo_imagem,lista_posicao[self.campo2]) # printar o campo
        janela.screen.blit(self.campo_imagem,lista_posicao[self.campo3]) # printar o campo
        janela.screen.blit(self.campo_imagem,lista_posicao[self.campo4]) # printar o campo
        janela.screen.blit(self.campo_imagem,lista_posicao[self.campo5]) # printar o campo
        janela.screen.blit(self.contorno_imagem,lista_posicao[self.contorno]) # printar o cursor
        janela.screen.blit(self.texto_nome,lista_posicao[self.campo1]) # printar nome
        janela.screen.blit(self.texto_login,lista_posicao[self.campo2]) # printar login
        janela.screen.blit(self.texto_senha,lista_posicao[self.campo3]) # printar senha
        janela.screen.blit(self.texto_email,lista_posicao[self.campo4]) # printar email
        janela.screen.blit(self.texto_nascimento,lista_posicao[self.campo5]) # printar nascimento

        if erro==0:
            self.texto_erro = self.fonte.render("Campo em Branco ou Login ja Existe",1,(0,0,0))
            janela.screen.blit(self.texto_erro,(75,400))
        if erro==1:
            self.texto_erro = self.fonte.render("Cadastro Efetuado Com 'sUceSsU' ",1,(0,0,0))
            janela.screen.blit(self.texto_erro,(75,400))
