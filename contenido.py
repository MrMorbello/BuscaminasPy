class Contenido:
    def __init__(self):
        self.marcado = False

    def establecer_numero(self, numero):
        pass

    def marcar(self):
        self.marcado = not self.marcado

    def activar(self):
        pass
    
    def esta_marcado(self):
        return self.marcado


class Bomba(Contenido):

    def __init__(self, juego):
        super().__init__()
        self.juego = juego

    def activar(self):
        self.juego.perder()


class Numero(Contenido):

    def __init__(self):
        super().__init__()
        self.numero = None
    
    def establecer_numero(self, numero):
        self.numero = numero
