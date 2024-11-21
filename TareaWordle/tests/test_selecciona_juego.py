from app.Wordle import Wordle

#primer test para el tdd
# def test_selecciona_juego1():
#     wordle = Wordle()
#     wordle.palabraJuego = wordle.selecciona_juego()
#     assert wordle.palabraJuego == "JAMON"

def test_selecciona_juego1():
    wordle = Wordle()
    wordle.selecciona_juego()
    assert wordle.palabraJuego in Wordle.PALABRAS



