from constantes import *

class Contenido:
    def __init__(self):
        self.marcado = False

    def incrementar_numero(self):
        pass

    def marcar(self):
        self.marcado = not self.marcado

    def activar(self):
        pass
    
    def esta_marcado(self):
        return self.marcado

    def dibujo(self):
        pass


class Bomba(Contenido):

    def __init__(self, juego):
        super().__init__()
        self.juego = juego

    def activar(self):
        self.juego.perder()
    
    def dibujo(self):
        return BOMBA


class Numero(Contenido):

    def __init__(self):
        super().__init__()
        self.numero = 0
    
    def incrementar_numero(self):
        self.numero += 1
    
    def dibujo(self):
        return VACIO if self.numero == 0 else self.numero
