__author__ = 'Douglas'
from util.CriaBotao import *

class TelaRecordNivel:
    def __init__(self):

        self.fonte = pygame.font.SysFont("comicsansms",20)
        self.fonte_titulo = pygame.font.SysFont("comicsansms",40)
        self.facil_imagem = CriarBotao("facil").cria_botao()
        self.medio_imagem = CriarBotao("medio").cria_botao()
        self.dificil_imagem = CriarBotao("dificil").cria_botao()
        self.voltar_imagem = CriarBotao("voltar").cria_botao()
        self.contorno_imagem = CriarBotao("contorno").cria_botao()
        self.i=0

        self.file_back=os.path.join("imagens","backrecord.png") #file recebe o local da imagem que sera utilizada
        self.back_imagem = pygame.image.load(self.file_back) # recebe a imagem do background

    def imprime_tela_record_nivel(self,janela,posicao,lista_nome_record_nivel):

        self.background,self.facil,self.medio,self.dificil,self.voltar,self.contorno=0,1,2,3,4,13
        self.titulo_meu_record,self.titulo_record_geral,self.meu_record,self.record1,self.record2,self.record3,self.record4,self.record5=5,6,7,8,9,10,11,12
        self.lista_nome_record=lista_nome_record_nivel
        #self.texto_titulo_meu_record=self.fonte_titulo.render("Meu Record",1,(255,255,255))
        self.texto_titulo_record_geral=self.fonte_titulo.render("Record de Geral",1,(255,255,255))
        janela.screen.blit(self.back_imagem,posicao[self.background])

        while self.lista_nome_record != None and self.i<len(self.lista_nome_record):

            self.texto_meu_record = self.fonte.render((str(self.lista_nome_record[self.i][0])+" => "+str(self.lista_nome_record[self.i][1])+"s"),1,(255,255,255))
            self.posicao_tela=self.i+7
            janela.screen.blit(self.texto_meu_record,posicao[self.posicao_tela])
            self.i=self.i+1

        if self.i>=len(self.lista_nome_record):
            self.i=0

        janela.screen.blit(self.facil_imagem,posicao[self.facil])
        janela.screen.blit(self.medio_imagem,posicao[self.medio])
        janela.screen.blit(self.dificil_imagem,posicao[self.dificil])
        janela.screen.blit(self.voltar_imagem,posicao[self.voltar])
       # janela.screen.blit(self.texto_titulo_meu_record,posicao[self.titulo_meu_record])
        janela.screen.blit(self.texto_titulo_record_geral,posicao[self.titulo_record_geral])
        janela.screen.blit(self.contorno_imagem,posicao[self.contorno]) # printar o contorno