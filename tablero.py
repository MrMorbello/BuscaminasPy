from contenedor import Contenedor

def diccionario_de_contenedores(ancho, alto):
    return {(x, y): Contenedor((x, y)) for x in range(alto) for y in range(alto)}

def iterar_vecinos(casilleros, pos):
    vecinos = [
            (pos[0] - 1, pos[1] - 1), 
            (pos[0] + 1, pos[1] + 1),
            (pos[0] + 1, pos[1] - 1),
            (pos[0] - 1, pos[1] + 1), 
            (pos[0] - 1, pos[1]), 
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1), 
            (pos[0], pos[1] - 1), 
        ]
    for vecino in vecinos: 
        casilleros.get(vecino, Contenedor(vecino)).incrementar_numero()


class Tablero():
    def __init__(self, juego) -> None:
        self.juego = juego
        self.casilleros = diccionario_de_contenedores(juego.ancho, juego.alto)
        self.meter_bomba()

    def actualizar_numeros(self, ubicacion):
        iterar_vecinos(self.casilleros, ubicacion)

    def click(self, ubicacion):
        self.casilleros.get(ubicacion).descubrir()

    def marcar(self, ubicacion):
        self.casilleros.get(ubicacion).marcar()

    def meter_bomba(self):
        # Prueba de bomba
        self.casilleros[(1, 1)].guardar_bomba(self.juego)
        self.actualizar_numeros((1, 1))

    def dibujar(self):
        for linea in range(self.juego.alto):
            print('| ', end='')
            for columna in range(self.juego.ancho):
                self.casilleros.get((linea, columna)).dibujar()
            print('|')
    