from cci.ControleTeclado import *
from CriarJanela import *

class TentaTeclado:
    def __init__(self):
        self.teclado=ControleTeclado()

    def rodaTeclado(self):
        self.teclado.captura_evento()
        if self.teclado.teclas[7] == "c":
            print(self.teclado.teclas[7])

criarJanela=CriarJanela((632,632),"Tenta")
tenta=TentaTeclado()
while True:
   tenta.rodaTeclado()