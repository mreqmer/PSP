import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parchis.ParchisClase import ParchisClase

def test_es_ganador1():
    parchis = ParchisClase("juan", "pepe")
    parchis.ficha_j1 = ParchisClase.TAM_TABLERO
    parchis.ficha_j2 = 4
    cadena = parchis.es_ganador()
    assert cadena == "juan"

def test_es_ganador2():
    parchis = ParchisClase("juan", "pepe")
    parchis.ficha_j1 = 19
    parchis.ficha_j2 = ParchisClase.TAM_TABLERO
    cadena = parchis.es_ganador()
    assert cadena == "pepe"

def test_es_ganador3():
    parchis = ParchisClase("juan", "pepe")
    parchis.ficha_j1 = 19
    parchis.ficha_j2 = 19
    cadena = parchis.es_ganador()
    assert cadena == ""