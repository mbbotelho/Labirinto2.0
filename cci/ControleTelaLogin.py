__author__ = 'Douglas'


from ControleTeclado import *
from cgt.AplGerenciarPessoa import *
from cih.TelaLogin import *




class ControleLogin:

    def __init__(self):

        self.tela_login=CriarTelaLogin()
        self.teclado=ControleTeclado()
        self.apl_pessoa=AplGerenciarPessoa()
                                  #Backg  #Login    #Senha   #Confirmar #Limpar  #Cadastrar #Campo1 #Campo2  #Contorno
        self.posicao_imagens_login=[(0,0),(50,150),(50,250),(250,350),(360,350),(470,350),(200,150),(200,250),[50,150]] # Lista com as posicoes dos botoes
        self.erro=False

    def controla_imagens_login(self,janela,lista_login_senha,opcao):

        self.opcao=opcao

        self.teclado.captura_evento()
        background,login,senha,confirmar,limpar,cadastrar,campo1,campo2,contorno=0,1,2,3,4,5,6,7,8
        self.altura=1
        self.largura=0
        velocidade_contorno_altura=100
        velocidade_contorno_largura=110
        self.cima,self.baixo,self.esquerda,self.direita,self.esc,self.espaco,self.letras=0,1,2,3,4,6,7


        if self.teclado.teclas[self.cima] and self.posicao_imagens_login[contorno][self.altura] > self.posicao_imagens_login[login][self.altura] and self.posicao_imagens_login[contorno][self.altura] < self.posicao_imagens_login[confirmar][self.altura]:
            self.posicao_imagens_login[contorno][self.altura]-=velocidade_contorno_altura

        elif self.teclado.teclas[self.baixo] and self.posicao_imagens_login[contorno][self.altura] < self.posicao_imagens_login[senha][self.altura]:
            self.posicao_imagens_login[contorno][self.altura]+=velocidade_contorno_altura

        elif self.teclado.teclas[self.baixo] and self.posicao_imagens_login[contorno][self.altura] == self.posicao_imagens_login[senha][self.altura]:
            self.posicao_imagens_login[contorno][self.altura]= self.posicao_imagens_login[confirmar][self.altura]
            self.posicao_imagens_login[contorno][self.largura]= self.posicao_imagens_login[confirmar][self.largura]

        elif self.teclado.teclas[self.cima] and self.posicao_imagens_login[contorno][self.altura] == self.posicao_imagens_login[confirmar][self.altura]:
            self.posicao_imagens_login[contorno][self.altura]= self.posicao_imagens_login[senha][self.altura]
            self.posicao_imagens_login[contorno][self.largura]= self.posicao_imagens_login[senha][self.largura]

        elif self.teclado.teclas[self.direita] and (self.posicao_imagens_login[contorno][self.altura] == self.posicao_imagens_login[confirmar][self.altura] and self.posicao_imagens_login[contorno][self.largura] < self.posicao_imagens_login[cadastrar][self.largura]):
            self.posicao_imagens_login[contorno][self.largura]+=velocidade_contorno_largura

        elif self.teclado.teclas[self.esquerda] and (self.posicao_imagens_login[contorno][self.altura] == self.posicao_imagens_login[confirmar][self.altura] and self.posicao_imagens_login[contorno][self.largura] > self.posicao_imagens_login[confirmar][self.largura]):
            self.posicao_imagens_login[contorno][self.largura]-=velocidade_contorno_largura

        pessoa_logada=self.controle_se_loga(janela,lista_login_senha)
        return pessoa_logada

    def controle_se_loga(self,janela,lista_login_senha):


        self.teclado.captura_evento()
        self.loginl,self.senhal=0,1
        self.lista_login=lista_login_senha
        background,login,senha,confirmar,limpar,cadastrar,campo1,campo2,contorno=0,1,2,3,4,5,6,7,8

        self.tela_login.imprime_tela_login(janela,self.posicao_imagens_login,lista_login_senha,self.erro)

        if self.teclado.teclas[self.letras] != "":

            if self.posicao_imagens_login[contorno][self.altura] == self.posicao_imagens_login[login][self.altura]:
                if self.teclado.teclas[self.letras] == "\x08": # \x08 e a tecla backspace (apagar)
                    self.tamanho=len(self.lista_login[self.loginl])
                    self.palavra=self.lista_login[self.loginl]
                    self.lista_login[self.loginl]=self.palavra[:self.tamanho-1]
                else:
                    self.lista_login[self.loginl]+=self.teclado.teclas[self.letras]
            elif self.posicao_imagens_login[contorno][self.altura] == self.posicao_imagens_login[senha][self.altura]:
                if self.teclado.teclas[self.letras] == "\x08":
                    self.tamanho=len(self.lista_login[self.senhal])
                    self.palavra=self.lista_login[self.senhal]
                    self.lista_login[self.senhal]=self.palavra[:self.tamanho-1]
                else:
                    self.lista_login[self.senhal]+=self.teclado.teclas[self.letras]

        if self.teclado.teclas[self.espaco]:
            if self.posicao_imagens_login[contorno][self.altura]==self.posicao_imagens_login[confirmar][self.altura] and self.posicao_imagens_login[contorno][self.largura]==self.posicao_imagens_login[confirmar][self.largura]:
                self.pessoa_logada=self.apl_pessoa.login_pessoa(self.lista_login)
                if self.pessoa_logada==None:
                    self.erro=True
                else:
                    self.opcao=3
                    return self.pessoa_logada #(Nome,login,senha,data_nascimento,email)

            if self.posicao_imagens_login[contorno][self.altura]==self.posicao_imagens_login[limpar][self.altura] and self.posicao_imagens_login[contorno][self.largura]==self.posicao_imagens_login[limpar][self.largura]:
                self.lista_login[self.loginl],self.lista_login[self.senhal]="",""
                return self.lista_login

            if self.posicao_imagens_login[contorno][self.altura]==self.posicao_imagens_login[cadastrar][self.altura] and self.posicao_imagens_login[contorno][self.largura]==self.posicao_imagens_login[cadastrar][self.largura]:
                self.opcao=2
                return self.opcao
        if self.teclado.teclas[self.esc]:
            pygame.quit()
            sys.exit()

