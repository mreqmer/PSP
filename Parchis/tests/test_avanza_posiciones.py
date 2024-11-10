import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parchis.ParchisClase import ParchisClase

def test_avanza_posiciones1():
    parchis = ParchisClase("juan", "pepe")
    posicionAntigua = parchis.ficha_j1
    parchis.tira_dados()
    res_dados = parchis.dado1 + parchis.dado2
    parchis.avanza_posiciones(parchis, 1)
    assert parchis.ficha_j1 == (posicionAntigua + res_dados)

def test_avanza_posiciones2():
    parchis = ParchisClase("juan", "pepe")
    parchis.tira_dados()
    res_dados = parchis.dado1 + parchis.dado2
    posicionAntigua = parchis.ficha_j1
    parchis.avanza_posiciones(parchis, 1)
    assert parchis.ficha_j1 == (posicionAntigua + res_dados)


