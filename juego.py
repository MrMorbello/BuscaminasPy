from contenedor import Contenedor
from constantes import *

class Juego:

    def __init__(self, alto=4, ancho=4):
        self.estado = EN_JUEGO
        self.alto = alto
        self.ancho = ancho
        self.contenedores = {}

    def perder(self):
        self.estado = PERDIDO
        # Mostrar bombas y romper todo :(
    
    def ganar(self):
        self.estado = GANADO
        # Ganar (?

    def click(self, ubicacion):
        self.contenedores.get(ubicacion).click()

    def marcar(self, ubicacion):
        self.contenedores.get(ubicacion).marcar()