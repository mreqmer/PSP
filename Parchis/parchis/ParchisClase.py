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

    @staticmethod
    def tira_dados():
        ParchisClase.dado1 = randint(1,6)
        ParchisClase.dado2 = randint(1,6)


    @staticmethod
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

    @staticmethod
    def avanza_posiciones(self, turno):
        self.ficha_j1 = ParchisClase.dado1 + ParchisClase.dado2






