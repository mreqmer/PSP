import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parchis.ParchisClase import ParchisClase

def test_avanza_posiciones1():
    parchis = ParchisClase("juan", "pepe")
    parchis.ficha_j1 = 8
    ParchisClase.dado1 = 2
    ParchisClase.dado2 = 4
    parchis.avanza_posiciones(1)
    assert parchis.ficha_j1 == 14

def test_avanza_posiciones2():
    parchis = ParchisClase("juan", "pepe")
    parchis.ficha_j2 = 8
    ParchisClase.dado1 = 2
    ParchisClase.dado2 = 4
    parchis.avanza_posiciones(2)
    assert parchis.ficha_j2 == 14

def test_avanza_posiciones3():
    parchis = ParchisClase("juan", "pepe")
    posicionAntigua = parchis.ficha_j1
    ParchisClase.tira_dados()
    res_dados = parchis.dado1 + parchis.dado2
    parchis.avanza_posiciones(1)
    assert parchis.ficha_j1 == (posicionAntigua + res_dados)

def test_avanza_posiciones4():
    parchis = ParchisClase("juan", "pepe")
    posicionAntigua = parchis.ficha_j2
    ParchisClase.tira_dados()
    res_dados = parchis.dado1 + parchis.dado2
    parchis.avanza_posiciones(2)
    assert parchis.ficha_j2 == (posicionAntigua + res_dados)

def test_avanza_posiciones5():
    parchis = ParchisClase("juan", "pepe")
    parchis.ficha_j1 = 16
    ParchisClase.dado1 = 5
    ParchisClase.dado2 = 5
    parchis.avanza_posiciones(1)
    assert parchis.ficha_j1 == 14










