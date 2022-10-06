class Minas():
    def __init__(self):
        self.victoria = True
    def perder(self) -> None:
        """
        Termina el juego.
        """
        print("Perdiste, has estallado.")
        self.victoria = False
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
    
    def jugar(self) -> None:
        """
        Comienza una partida.
        """
        fila = int(input("Digite un número de fila entre 0 y 4."))
        while(fila > -1 and fila > 4):
            fila = int(input("Digite un número de fila entre 0 y 4."))
        columna = int(input("Digite un número de columna entre 0 y 4."))
        while(columna > -1 and columna > 4):
            columna = int(input("Digite un número de columna entre 0 y 4."))
        if self.casilla[fila][columna] == 1:
            self.perder()
        elif self.casilla[fila][columna] == 2:
            print("Ya habías jugado en esta casilla, prueba otra.")
        else:
            print("Eso estuvo cerca, sigue jugando por ahora.")
            self.casilla[fila][columna] = 2
        
            
