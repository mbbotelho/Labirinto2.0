from cci.ControleTeclado import *


class TesteTeclado:

    def rodaTeclado(self):
        cima=0
        self.teclado=ControleTeclado()
        self.teclado.captura_evento()
        if self.teclado.teclas[cima] == False:
            return True

    def rodaTeclado_baixo(self):
        baixo=0
        self.teclado=ControleTeclado()
        self.teclado.captura_evento()
        if self.teclado.teclas[baixo] == False:
            return False

    def rodaTeclado_esquerda(self):
        esquerda=0
        self.teclado=ControleTeclado()
        self.teclado.captura_evento()
        if self.teclado.teclas[esquerda] == False:
            return True

    def rodaTeclado_direita(self):
        direita=0
        self.teclado=ControleTeclado()
        self.teclado.captura_evento()
        if self.teclado.teclas[direita] == False:
            return True