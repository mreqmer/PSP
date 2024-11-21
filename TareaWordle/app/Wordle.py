from random import randint

class Wordle:

    PALABRAS = ["ANGEL", "JAMON", "LENTO", "VERDE", "PLAYA", "HIELO", "FUEGO", "MANGO", "BANCO", "SALTO"]


    def __init__(self):
        self.palabraJuego = ""
        self.pistas = [["-----", "-----" ], ["-----", "-----"], ["-----", "-----"],
                       ["-----", "-----"], ["-----", "-----"], ["-----", "-----"]]
        self.numIntento = 0

    def selecciona_juego(self):

        seleccion = randint(0, 9)
        self.palabraJuego = Wordle.PALABRAS[seleccion]

    def realiza_intento(self, palabra_intento):
        pista_vacia = "-----"
        nueva_pista = ""
        palabra_mayus = str(palabra_intento.upper())

        self.pistas[self.numIntento][0] = palabra_mayus

        for i in range(0, len(pista_vacia)):
            if palabra_mayus[i] == self.palabraJuego[i]:
                nueva_pista += palabra_mayus[i]
            elif palabra_mayus[i] in self.palabraJuego:
                nueva_pista += "*"
            else:
                nueva_pista += "-"

        self.pistas[self.numIntento][1] = nueva_pista
        self.numIntento += 1



