from constantes import *

class Estado:
    def __init__(self, contenedor):
        self.contenedor = contenedor

    def click(self):
        pass

    def marcar(self):
        pass

class Oculto(Estado):
    def click(self):
        self.contenedor.pasar_estado_a_descubierto()
    
    def marcar(self):
        self.contenedor.pasar_estado_a_marcado()

    def dibujo(self):
        return NO_DESCUBIERTO

class Descubierto(Estado):
    def dibujo(self):
        return self.contenedor.dibujo()

class Marcado(Estado):
    def marcar(self):
        self.contenedor.pasar_estado_a_oculto()
    
    def dibujo(self):
        return MARCA
