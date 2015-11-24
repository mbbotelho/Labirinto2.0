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

        self.file_back=os.path.join("imagens","backrecord.png") #file recebe o local da imagem que sera utilizada
        self.back_imagem = pygame.image.load(self.file_back) # recebe a imagem do background

    def imprime_tela_record_nivel(self,janela,posicao,lista_nome_record_nivel):

        self.lista_nome_record=lista_nome_record_nivel

        meu_record,record1,record2,record3,record4,record5=0,1,2,3,4,5

        self.texto_titulo_meu_record=self.fonte_titulo.render("Meu Record",1,(255,255,255))
        self.texto_titulo_record_geral=self.fonte_titulo.render("Record de Geral",1,(255,255,255))
        if self.lista_nome_record != None:
            self.texto_meu_record = self.fonte.render(str(self.lista_nome_record[meu_record]),1,(255,255,255))
            self.texto_record1 = self.fonte.render(str(self.lista_nome_record[record1]),1,(255,255,255))
            self.texto_record2 = self.fonte.render(str(self.lista_nome_record[record2]),1,(255,255,255))
            self.texto_record3 = self.fonte.render(str(self.lista_nome_record[record3]),1,(255,255,255))
#        self.texto_record4 = self.fonte.render(str(self.lista_nome_record[record4]),1,(255,255,255))
#        self.texto_record5 = self.fonte.render(str(self.lista_nome_record[record5]),1,(255,255,255))

        self.background,self.facil,self.medio,self.dificil,self.voltar,self.contorno=0,1,2,3,4,13
        self.titulo_meu_record,self.titulo_record_geral,self.meu_record,self.record1,self.record2,self.record3,self.record4,self.record5=5,6,7,8,9,10,11,12


        janela.screen.blit(self.back_imagem,posicao[self.background])
        janela.screen.blit(self.facil_imagem,posicao[self.facil])
        janela.screen.blit(self.medio_imagem,posicao[self.medio])
        janela.screen.blit(self.dificil_imagem,posicao[self.dificil])
        janela.screen.blit(self.voltar_imagem,posicao[self.voltar])
        janela.screen.blit(self.texto_titulo_meu_record,posicao[self.titulo_meu_record])
        janela.screen.blit(self.texto_titulo_record_geral,posicao[self.titulo_record_geral])
        if self.lista_nome_record != None:
            janela.screen.blit(self.texto_meu_record,posicao[self.meu_record])
            janela.screen.blit(self.texto_record1,posicao[self.record1])
            janela.screen.blit(self.texto_record2,posicao[self.record2])
            janela.screen.blit(self.texto_record3,posicao[self.record3])
            #janela.screen.blit(self.texto_record4,posicao[self.record4])
           # janela.screen.blit(self.texto_record5,posicao[self.record5])
        janela.screen.blit(self.contorno_imagem,posicao[self.contorno]) # printar o contorno