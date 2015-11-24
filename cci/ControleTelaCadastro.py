__author__ = 'Douglas'
from ControleTeclado import *
from cgt.AplGerenciarPessoa import *

class ControleCadastro:

    def __init__(self):
                                       #Backg #Nome    #Login   #Senha   #Email  #DtNasc  #Confirmar #Limpar  #Voltar   #Campo1   #Campo2    #Campo3   #Campo4  #Campo5   #Contorno
        self.posicao_imagens_cadastro=[(0,0),(50,150),(50,200),(50,250),(50,300),(50,350),(250,450),(360,450),(470,450),(200,150),(200,200),(200,250),(200,300),(200,350),[50,150]] # Lista com as posicoes dos botoes
        self.teclado=ControleTeclado()
        self.aplGerenciarPessoa = AplGerenciarPessoa()
        self.erro=3


    def controla_imagens_cadastro(self,opcao):

        self.opcao=opcao

        self.teclado.captura_evento()

        background,nome,login,senha,email,dataNascimento,confirmar,limpar,voltar,campo1,campo2,campo3,campo4,campo5,self.contorno=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
        self.altura=1
        self.largura=0
        self.velocidade_contorno_altura=50
        self.velocidade_contorno_largura=110
        self.cima,self.baixo,self.esquerda,self.direita,self.esc,self.espaco,self.letras=0,1,2,3,4,6,7


        if self.teclado.teclas[self.cima] and self.posicao_imagens_cadastro[self.contorno][self.altura] > self.posicao_imagens_cadastro[nome][self.altura] and self.posicao_imagens_cadastro[self.contorno][self.altura] < self.posicao_imagens_cadastro[confirmar][self.altura]:
            self.posicao_imagens_cadastro[self.contorno][self.altura]-=self.velocidade_contorno_altura

        elif self.teclado.teclas[self.baixo] and self.posicao_imagens_cadastro[self.contorno][self.altura] < self.posicao_imagens_cadastro[dataNascimento][self.altura]:
            self.posicao_imagens_cadastro[self.contorno][self.altura]+=self.velocidade_contorno_altura

        elif self.teclado.teclas[self.baixo] and self.posicao_imagens_cadastro[self.contorno][self.altura] == self.posicao_imagens_cadastro[dataNascimento][self.altura]:
            self.posicao_imagens_cadastro[self.contorno][self.altura]= self.posicao_imagens_cadastro[confirmar][self.altura]
            self.posicao_imagens_cadastro[self.contorno][self.largura]= self.posicao_imagens_cadastro[confirmar][self.largura]

        elif self.teclado.teclas[self.cima] and self.posicao_imagens_cadastro[self.contorno][self.altura] == self.posicao_imagens_cadastro[confirmar][self.altura]:
            self.posicao_imagens_cadastro[self.contorno][self.altura]= self.posicao_imagens_cadastro[dataNascimento][self.altura]
            self.posicao_imagens_cadastro[self.contorno][self.largura]= self.posicao_imagens_cadastro[dataNascimento][self.largura]

        elif self.teclado.teclas[self.direita] and (self.posicao_imagens_cadastro[self.contorno][self.altura] == self.posicao_imagens_cadastro[confirmar][self.altura] and self.posicao_imagens_cadastro[self.contorno][self.largura] < self.posicao_imagens_cadastro[voltar][self.largura]):
            self.posicao_imagens_cadastro[self.contorno][self.largura]+=self.velocidade_contorno_largura

        elif self.teclado.teclas[self.esquerda] and (self.posicao_imagens_cadastro[self.contorno][self.altura] == self.posicao_imagens_cadastro[confirmar][self.altura] and self.posicao_imagens_cadastro[self.contorno][self.largura] > self.posicao_imagens_cadastro[confirmar][self.largura]):
            self.posicao_imagens_cadastro[self.contorno][self.largura]-=self.velocidade_contorno_largura

    def controla_se_cadastra(self,listaCadastral):
        self.teclado.captura_evento()
        self.nomel,self.loginl,self.senhal,self.emaill,self.dataNascimentol=0,1,2,3,4
        self.listaCadastral=listaCadastral
        self.background,self.nome,self.login,self.senha,self.email,self.dataNascimento,self.confirmar,self.limpar,self.voltar,self.campo1,self.campo2,self.campo3,self.campo4,self.campo5,self.contorno=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14

        if self.teclado.teclas[self.letras] != "":
            if self.posicao_imagens_cadastro[self.contorno][self.altura] == self.posicao_imagens_cadastro[self.nome][self.altura]:
                if self.teclado.teclas[self.letras] == "\x08":
                    self.tamanho=len(self.listaCadastral[self.nomel])
                    self.palavra=self.listaCadastral[self.nomel]
                    self.listaCadastral[self.nomel]=self.palavra[:self.tamanho-1]
                else:
                    self.listaCadastral[self.nomel]+=self.teclado.teclas[self.letras]
                return self.listaCadastral
            elif self.posicao_imagens_cadastro[self.contorno][self.altura] == self.posicao_imagens_cadastro[self.login][self.altura]:
                if self.teclado.teclas[self.letras] == "\x08":
                    self.tamanho=len(self.listaCadastral[self.loginl])
                    self.palavra=self.listaCadastral[self.loginl]
                    self.listaCadastral[self.loginl]=self.palavra[:self.tamanho-1]
                else:
                    self.listaCadastral[self.loginl]+=self.teclado.teclas[self.letras]
                return self.listaCadastral
            elif self.posicao_imagens_cadastro[self.contorno][self.altura] == self.posicao_imagens_cadastro[self.senha][self.altura]:
                if self.teclado.teclas[self.letras] == "\x08":
                    self.tamanho=len(self.listaCadastral[self.senhal])
                    self.palavra=self.listaCadastral[self.senhal]
                    self.listaCadastral[self.senhal]=self.palavra[:self.tamanho-1]
                else:
                    self.listaCadastral[self.senhal]+=self.teclado.teclas[self.letras]
                return self.listaCadastral
            elif self.posicao_imagens_cadastro[self.contorno][self.altura] == self.posicao_imagens_cadastro[self.email][self.altura]:
                if self.teclado.teclas[self.letras] == "\x08":
                    self.tamanho=len(self.listaCadastral[self.emaill])
                    self.palavra=self.listaCadastral[self.emaill]
                    self.listaCadastral[self.emaill]=self.palavra[:self.tamanho-1]
                else:
                    self.listaCadastral[self.emaill]+=self.teclado.teclas[self.letras]
                return self.listaCadastral
            elif self.posicao_imagens_cadastro[self.contorno][self.altura] == self.posicao_imagens_cadastro[self.dataNascimento][self.altura]:
                if self.teclado.teclas[self.letras] == "\x08":
                    self.tamanho=len(self.listaCadastral[self.dataNascimentol])
                    self.palavra=self.listaCadastral[self.dataNascimentol]
                    self.listaCadastral[self.dataNascimentol]=self.palavra[:self.tamanho-1]
                else:
                    self.listaCadastral[self.dataNascimentol]+=self.teclado.teclas[self.letras]
                return self.listaCadastral


        if self.teclado.teclas[self.espaco]:
            if self.posicao_imagens_cadastro[self.contorno][self.altura]==self.posicao_imagens_cadastro[self.confirmar][self.altura] and self.posicao_imagens_cadastro[self.contorno][self.largura]==self.posicao_imagens_cadastro[self.confirmar][self.largura]:
                self.problema=self.aplGerenciarPessoa.Cadastrar_pessoa(self.listaCadastral)
                if self.problema==False:
                    self.erro=0
                else:
                    self.erro=1

            if self.posicao_imagens_cadastro[self.contorno][self.altura]==self.posicao_imagens_cadastro[self.voltar][self.altura] and self.posicao_imagens_cadastro[self.contorno][self.largura]==self.posicao_imagens_cadastro[self.voltar][self.largura]:
                self.opcao=1
                self.erro=3
                return self.opcao

            if self.posicao_imagens_cadastro[self.contorno][self.altura]==self.posicao_imagens_cadastro[self.limpar][self.altura] and self.posicao_imagens_cadastro[self.contorno][self.largura]==self.posicao_imagens_cadastro[self.limpar][self.largura]:
                self.listaCadastral[self.nomel],self.listaCadastral[self.loginl],self.listaCadastral[self.senhal],self.listaCadastral[self.emaill],self.listaCadastral[self.dataNascimentol]="","","","",""
                self.erro=3
                return self.listaCadastral



