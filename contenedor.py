import contenido

class Contenedor:

    def __init__(self):

        self.descubierto = False
        self.contenido = None

    def click(self):
        pass

    def marcar(self):
        if self.descubierto: return
        self.contenido.marcar()

    def descubrir(self):
        if self.contenido.esta_marcado(): return
        self.descubierto = True

    def guardar_bomba(self, juego):
        self.contenido = contenido.Bomba(juego)

