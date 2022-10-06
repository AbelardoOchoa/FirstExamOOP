class Minas():
    def __init__(self):
        self.victoria = True
    def boom(self) -> None:
        """
        Le informa al jugador que seleccionó una mina y estalló.
        """
        print("Perdiste, has estallado.")

class Tablero(Minas):
    def __init__(self) -> None:
        self.casilla = []
        
class Buscaminas(Tablero):
    def __init__(self) -> None:
        self.interfaz = Tablero()
    
class Jugador(Buscaminas):
    def __init__(self) -> None:
        self.victoria = True
        self.casilla=   [[1, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0], 
                        [0, 0, 1, 0, 0], 
                        [0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1]]
    def perder(self) -> None:
        """
        Termina el juego.
        """
        self.boom()
        self.victoria = False
    def ganar(self) -> None:
        """
        Le informa al jugador que ganó.
        """
        print("Felicidades, ganaste.")
        self.victoria = False
    
    def jugar(self) -> None:
        """
        Comienza una partida.
        """
        fila = 0
        columna = 0
        fila = int(input("Digite un número de fila entre 0 y 4.\n"))
        while(fila < 0 and fila > 4):
            fila = int(input("Digite un número de fila entre 0 y 4.\n"))
        columna = int(input("Digite un número de columna entre 0 y 4.\n"))
        while(columna < 0 and columna > 4):
            columna = int(input("Digite un número de columna entre 0 y 4.\n"))
        if self.casilla[fila][columna] == 1:
            self.perder()
        elif self.casilla[fila][columna] == 2:
            print("Ya habías jugado en esta casilla, prueba otra.")
        elif (0 not in self.casilla[0] and 
              0 not in self.casilla[1] and
              0 not in self.casilla[2] and
              0 not in self.casilla[3] and
              0 not in self.casilla[4]):
            self.ganar()
        else:
            self.casilla[fila][columna] = 2
            print("Eso estuvo cerca, sigue jugando por ahora.")
            