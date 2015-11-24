from cih.TelaAbertura import *
from util.CriarJanela import *

from ControleTelaLogin import *
from cih.TelaCadastro import *
from ControleTelaCadastro import *
from ControleTelaCreditos import *
from cih.TelaCreditos import *
from ControleTelaMenu import *
from cih.TelaMenu import *
from cih.TelaNivel import *
from ControleTelaNivel import *
from cih.TelaRecordNivel import *
from ControleTelaRecordNivel import *
from cih.TelaJogo import *
from ControleTelaJogo import *
from cdp.CriaCoodenadasIniciaisLabirinto import *
from ControleTelaDerrota import *
from cih.TelaDerrota import *
from cdp.Jogada import *
from cdp.Pessoa import *
from cgt.AplGerenciaJogada import *
from cgt.AplGerenciaNivel import *

class ControlePrincipal:
    def __init__(self):

        self.janela=CriarJanela((632,632),"Labirinto do Capeta")
        self.abertura=TelaAbertura().imprime_tela_abertura(self.janela)
        pygame.display.update()

        self.lista_login_senha=["",""]
        self.controle_login=ControleLogin()


        self.lista_cadastro=["","","","",""]
        self.controle_cadastro=ControleCadastro()
        self.cadastro=TelaCadastro()

        self.controle_creditos=ControleTelaCreditos()
        self.creditos=CriaTelaCreditos()

        self.pessoa_logada=Pessoa(0,'')
        self.nivel_escolhido=''

        self.apl_gerencia_jogada = AplGerenciaJogada()
        self.apl_gerencia_nivel=AplGerenciaNivel()

        self.main_clock = pygame.time.Clock()
        self.opcao=1

        self.inicializa()

    def inicializa(self):

        self.controle_menu=ControleTelaMenu()
        self.menu=CriaTelaMenu()

        self.controle_nivel=ControleTelaNivel()
        self.nivel=TelaNivel()

        self.controle_record_nivel=ControleTelaRecordNivel()
        self.record_nivel=TelaRecordNivel()

        self.controle_jogo=ControleTelaJogo()

        self.controle_derrota=ControleTelaDerrota()
        self.derrota=TelaDerrota()

        self.jogo=TelaJogo()

    def loop_principal(self):
        while True:
            self.janela.screen.fill(0) #limpar a tela

            if self.opcao==1:
                self.main_clock.tick(17)
                self.controle_login.controla_imagens_login(self.janela,self.lista_login_senha,self.opcao)


                self.opcao=self.controle_login.opcao

            elif self.opcao==2:
                self.main_clock.tick(17)
                self.controle_cadastro.controla_imagens_cadastro(self.opcao)
                self.controle_cadastro.controla_se_cadastra(self.lista_cadastro)
                self.cadastro.imprime_tela_cadastro(self.janela,self.controle_cadastro.posicao_imagens_cadastro,self.lista_cadastro,self.controle_cadastro.erro)
                self.opcao=self.controle_cadastro.opcao

            elif self.opcao==3:
                self.main_clock.tick(17)
                self.controle_menu.controla_menu(self.opcao)
                self.menu.imprime_tela_menu(self.janela,self.controle_menu.posicao_imagens_menu)
                self.opcao=self.controle_menu.opcao

            elif self.opcao==4:
                self.main_clock.tick(17)
                self.controle_nivel.controle_tela_nivel(self.opcao)
                self.nivel.imprime_tela_nivel(self.janela,self.controle_nivel.posicao_imagens_nivel)
                self.opcao=self.controle_nivel.opcao

                if self.opcao==9:
                    self.coordenadas_objetos_labirinto=CoordenadasObjetosLabirinto(10,10)
                    self.lista_posicao_elementos_labirinto=self.coordenadas_objetos_labirinto.objetos(5)
                    self.nivel_escolhido=self.apl_gerencia_nivel.retorna_id("Facil")
                    self.opcao=8
                elif self.opcao==10:
                    self.coordenadas_objetos_labirinto=CoordenadasObjetosLabirinto(15,15)
                    self.lista_posicao_elementos_labirinto=self.coordenadas_objetos_labirinto.objetos(10)
                    self.nivel_escolhido=self.apl_gerencia_nivel.retorna_id("Medio")
                    self.opcao=8
                elif self.opcao==11:
                    self.coordenadas_objetos_labirinto=CoordenadasObjetosLabirinto(20,20)
                    self.lista_posicao_elementos_labirinto=self.coordenadas_objetos_labirinto.objetos(15)
                    self.nivel_escolhido=self.apl_gerencia_nivel.retorna_id("Dificil")
                    self.opcao=8

            elif self.opcao==6:
                self.main_clock.tick(17)
                self.controle_creditos.controla_creditos(self.opcao)
                self.creditos.imprime_tela_creditos(self.janela,self.controle_creditos.posicao_imagens_creditos)
                self.opcao=self.controle_creditos.opcao

            elif self.opcao==7:
                self.main_clock.tick(17)
                self.controle_record_nivel.controla_record_nivel(self.opcao)
                self.record_nivel.imprime_tela_record_nivel(self.janela,self.controle_record_nivel.posicao_imagens_record_nivel,self.controle_record_nivel.lista_nome_record)
                self.opcao=self.controle_record_nivel.opcao

            elif self.opcao==8:
                self.tempo=self.controle_jogo.controlador_player(self.lista_posicao_elementos_labirinto,self.opcao)
                self.jogo.imprime_tela_jogo(self.janela,self.lista_posicao_elementos_labirinto)
                self.opcao=self.controle_jogo.opcao

            elif self.opcao==9:
                jogada=Jogada(self.pessoa_logada.id,self.nivel_escolhido,self.tempo)
                self.apl_gerencia_jogada.Inserir_jogada(jogada)
                self.inicializa()
                self.opcao=3

            elif self.opcao==10:
                self.inicializa()
                self.opcao=11

            elif self.opcao==11:
                self.controle_derrota.controla_derrota(self.opcao)
                self.derrota.imprime_tela_derrota(self.janela,self.controle_derrota.posicao_imagens_derrota)
                self.opcao=self.controle_derrota.opcao


            pygame.display.update() # atualiza a tela
            self.main_clock.tick(20)

controle=ControlePrincipal()
while True:
    controle.loop_principal()

