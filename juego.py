from tablero import Tablero
from constantes import *

class Juego:

    def __init__(self, alto=4, ancho=4):
        self.estado = EN_JUEGO
        self.alto = alto
        self.ancho = ancho
        self.tablero = Tablero(self)

    def perder(self):
        self.estado = PERDIDO
        # Mostrar bombas y romper todo :(
    
    def ganar(self):
        self.estado = GANADO
        # Ganar (?

    def click(self, ubicacion):
        self.tablero.click(ubicacion)

    def marcar(self, ubicacion):
        self.tablero.marcar(ubicacion)

    def dibujar(self):
        self.tablero.dibujar()