import contenido
from constantes import *

class Contenedor:

    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.descubierto = False
        self.contenido = contenido.Numero()

    def incrementar_numero(self):
        self.contenido.incrementar_numero()

    def marcar(self):
        if self.descubierto: return
        self.contenido.marcar()

    def descubrir(self):
        if self.contenido.esta_marcado(): return
        self.contenido.activar()
        self.descubierto = True

    def guardar_bomba(self, juego):
        self.contenido = contenido.Bomba(juego)

    def dibujar(self):
        if self.descubierto: 
            self.contenido.dibujar()
        else:
            print(NO_DESCUBIERTO, end=' ')