__author__ = 'Douglas'
from ControleTeclado import *
from cgt.AplGerenciaRecord import *

class ControleTelaRecordNivel:

    def __init__(self):
                                          #Backg  #facil  #medio  #dificil #voltar  #TmeuRec #TrecGer #meuRec  #rec1    #rec2    #rec3   #rec4     #rec5   #Contorno
        self.posicao_imagens_record_nivel=[(0,0),(50,30),(160,30),(270,30),(380,30),(50,100),(50,220),(50,165),(50,280),(50,330),(50,380),(50,430),(50,480),[50,30]] # Lista com as posicoes dos botoes
        self.lista_nome_record=None
        self.teclado=ControleTeclado()
        self.apl_gerencia_record=AplGerenciaRecord()

    def controla_record_nivel(self,opcao):

        self.opcao=opcao
        self.teclado.captura_evento()

        self.esquerda,self.direita,self.esc,self.espaco=2,3,4,6
        self.background,self.facil,self.medio,self.dificil,self.voltar,self.contorno=0,1,2,3,4,13
        self.largura=0
        self.velocidade_largura=110

        if self.teclado.teclas[self.esquerda] and self.posicao_imagens_record_nivel[self.contorno][self.largura] > self.posicao_imagens_record_nivel[self.facil][self.largura]:
            self.posicao_imagens_record_nivel[self.contorno][self.largura]-=self.velocidade_largura

        if self.teclado.teclas[self.direita] and self.posicao_imagens_record_nivel[self.contorno][self.largura] < self.posicao_imagens_record_nivel[self.voltar][self.largura]:
            self.posicao_imagens_record_nivel[self.contorno][self.largura]+=self.velocidade_largura

        if self.posicao_imagens_record_nivel[self.contorno][self.largura]==self.posicao_imagens_record_nivel[self.facil][self.largura]:
            self.lista_nome_record=self.apl_gerencia_record.record("Facil")

        elif self.posicao_imagens_record_nivel[self.contorno][self.largura]==self.posicao_imagens_record_nivel[self.medio][self.largura]:
            self.lista_nome_record=self.apl_gerencia_record.record("Medio")

        elif self.posicao_imagens_record_nivel[self.contorno][self.largura]==self.posicao_imagens_record_nivel[self.dificil][self.largura]:
            self.lista_nome_record=self.apl_gerencia_record.record("Dificil")

        if self.teclado.teclas[self.espaco]: # se a tecla Space for pressionada
            if self.posicao_imagens_record_nivel[self.contorno][self.largura]==self.posicao_imagens_record_nivel[self.voltar][self.largura]:
                self.opcao=3
                return self.opcao

