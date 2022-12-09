import contenido, estado
from constantes import *

class Contenedor:
    # Main protocol
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.estado = estado.Oculto(self)
        self.contenido = contenido.Numero()

    def marcar(self):
        self.estado.marcar()

    def click(self):
        self.estado.click()


    # Seteo de estado
    def pasar_estado_a_descubierto(self):
        self.estado = estado.Descubierto(self)

    def pasar_estado_a_marcado(self):
        self.estado = estado.Marcado(self)

    def pasar_estado_a_oculto(self):
        self.estado = estado.Oculto(self)

    # Seteo de contenido
    def incrementar_numero(self):
        self.contenido.incrementar_numero()

    def guardar_bomba(self, juego):
        self.contenido = contenido.Bomba(juego)

    def dibujar(self):
        print(self.estado.dibujo(), end=' ')
    
    def dibujo(self):
        return self.contenido.dibujo()