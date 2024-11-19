from random import randint


class ParchisClase:

    TAM_TABLERO = 20
    #Atributos estáticos
    dado1 = 0
    dado2 = 0

    #Atributos no estáticos y constuctor con los nombres de los jugadores
    def __init__ (self, nombre_j1, nombre_j2):
        self.ficha_j1 = 0
        self.ficha_j2 = 0
        self.nombre_j1 = nombre_j1
        self.nombre_j2 = nombre_j2

    """
    Hace una tirada aleatoria de los dados
    """
    @staticmethod
    def tira_dados():
        ParchisClase.dado1 = randint(1,6)
        ParchisClase.dado2 = randint(1,6)

    """
    Dibuja en la consola el tablero donde se juega
    :return cadena con el tablero de juego
    """
    def pinta_tablero(self):
       cadena = ""

        #bucle de la fila donde aparecen las posiciones
       for i in range(ParchisClase.TAM_TABLERO + 1):
           if i == 0:
              cadena += "\t\t" + "I"
           elif i == ParchisClase.TAM_TABLERO:
               cadena += "\t" + "F"
           else:
               cadena += "\t" + str(i)
       #salto de linea y bucle para la fila del j1
       cadena += "\n"
       cadena += self.nombre_j1+ "\tI"
       for i in range(1, ParchisClase.TAM_TABLERO + 1):
           cadena += "\t"
           if i == self.ficha_j1:
               cadena += "O"
           elif i == ParchisClase.TAM_TABLERO:
              cadena += "F"
       # salto de linea y bucle para la fila del j2
       cadena += "\n"
       cadena += self.nombre_j2 + "\tI"
       for i in range(1, ParchisClase.TAM_TABLERO + 1):
           cadena += "\t"
           if i == self.ficha_j2:
               cadena += "O"
           elif i == ParchisClase.TAM_TABLERO:
               cadena += "F"
       return cadena

    """
    Avanza las fichas dependiendo de a quien le toque en ese turno.
    :param turno 1 para jugador_1, cualquier otro para el jugador_2
    """
    def avanza_posiciones(self, turno):

        if(turno == 1):
            self.ficha_j1 = self.ficha_j1 + ParchisClase.dado1 + ParchisClase.dado2
            if(self.ficha_j1 > ParchisClase.TAM_TABLERO):
                rebote = self.ficha_j1-ParchisClase.TAM_TABLERO
                self.ficha_j1 = ParchisClase.TAM_TABLERO - rebote
        else:
            self.ficha_j2 = self.ficha_j2 + ParchisClase.dado1 + ParchisClase.dado2
            if(self.ficha_j2 > ParchisClase.TAM_TABLERO):
                rebote = self.ficha_j2 - ParchisClase.TAM_TABLERO
                self.ficha_j2 = ParchisClase.TAM_TABLERO - rebote

    """
    Va informando del estado de la carrera
    :return cadena con el estado de la carrera
    """
    def estado_carrera(self):

        if (self.ficha_j1 > self.ficha_j2):
            cadena = f"{self.nombre_j1} va ganando"
        elif (self.ficha_j2 > self.ficha_j1):
            cadena = f"{self.nombre_j2} va ganando"
        else:
            cadena = "Empate!"
        return cadena

    """
    Informa de si ha habido un ganador en la partida
    :return cadena con el nombre del ganador, o "" si no ha habido ganador
    """
    def es_ganador(self):
        if (self.ficha_j1 == ParchisClase.TAM_TABLERO):
            cadena = f"{self.nombre_j1}"
        elif (self.ficha_j2 == ParchisClase.TAM_TABLERO):
            cadena = f"{self.nombre_j2}"
        else:
            cadena = ""
        return cadena





