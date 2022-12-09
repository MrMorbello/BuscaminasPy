from juego import Juego
juego = Juego()

juego.click((0,0))
juego.click((0,1))
juego.click((1,1))
juego.marcar((0,3))
juego.click((0,3))
juego.marcar((0,3))
juego.dibujar()
