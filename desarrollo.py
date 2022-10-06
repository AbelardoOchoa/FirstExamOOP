class Buscaminas():
    def __init__(self) -> None:
        self.interfaz = Tablero()

class Tablero():
    def __init__(self) -> None:
        self.casilla = [0, 1, 0, 1, 0][1, 0, 1, 0, 1]
    

class Minas():
    def __init__(self) -> None:
        ...
    def perder(self) -> None:
        self.victoria = False
    def boom(self) -> None:
        print("Perdiste, has estallado.")
            

class Jugador():
    def __init__(self) -> None:
        self.victoria = True
    
    def jugar(self, fila, columna):
        if self.casilla[fila][columna] == 1:
            self.perder()
        elif self.casilla[fila][columna] == 2:
            print("Ya habías jugado en esta casilla, prueba otra.")
        else:
            print("Eso estuvo cerca, sigue jugando por ahora.")
            self.casilla[fila][columna] = 2
        
            
