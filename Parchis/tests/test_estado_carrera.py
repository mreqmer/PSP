import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parchis.ParchisClase import ParchisClase

def test_estado_carrera1():
    parchis = ParchisClase("juan", "pepe")
    parchis.ficha_j1 = 5
    parchis.ficha_j2 = 4
    cadena = parchis.estado_carrera()
    assert cadena == "juan va ganando"

def test_estado_carrera2():
    parchis = ParchisClase("juan", "pepe")
    parchis.ficha_j1 = 0
    parchis.ficha_j2 = 0
    cadena = parchis.estado_carrera()
    assert cadena == "Empate!"

def test_estado_carrera3():
    parchis = ParchisClase("juan", "pepe")
    parchis.ficha_j1 = 1
    parchis.ficha_j2 = 3
    cadena = parchis.estado_carrera()
    assert cadena == "pepe va ganando"