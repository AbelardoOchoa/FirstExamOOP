from desarrollo import Buscaminas, Tablero, Minas, Jugador
posada = Jugador()
juego = Buscaminas()
tablero = Tablero()

while(posada.victoria):
    posada.jugar()