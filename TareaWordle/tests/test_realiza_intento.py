from app.Wordle import Wordle

#primer test para comprobar que se aumentan correctamente los intentos
def test_realiza_intento1():
    palabra = "jabon"
    wordle = Wordle()
    wordle.selecciona_juego()
    wordle.realiza_intento(palabra)
    assert wordle.numIntento == 1
#test que comprueba que el primer intento se coloque bien (sin comprobar la columna donde está)
#la pista
def test_realiza_intento2():
    palabra = "jabon"
    wordle = Wordle()
    wordle.palabraJuego = "JAMON"
    wordle.realiza_intento(palabra)
    assert wordle.pistas[0][0] == palabra.upper()

#test que comprueba que el primer intento se coloque bien, comprobando que la pista se haya puesto bien
def test_realiza_intento3 ():
    palabra = "jabon"
    wordle = Wordle()
    wordle.palabraJuego = "JAMON"
    wordle.realiza_intento(palabra)
    assert wordle.pistas[0] == [palabra.upper(), "JA-ON"]

#Comprobacion con asteriscos
def test_realiza_intento4():
    palabra = "amore"
    wordle = Wordle()
    wordle.palabraJuego = "JAMON"
    wordle.realiza_intento(palabra)
    assert wordle.pistas[0] == [palabra.upper(), "***--"]

#Comprobacion con asteriscos
def test_realiza_intento5():
    palabra = "ammre"
    wordle = Wordle()
    wordle.palabraJuego = "JAMON"
    wordle.realiza_intento(palabra)
    assert wordle.pistas[0] == [palabra.upper(), "**M--"]

