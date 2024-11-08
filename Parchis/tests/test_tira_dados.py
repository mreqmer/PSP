import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parchis.ParchisClase import ParchisClase


def test_tira_dados():
    # Ejecuta el método que deseas probar
    ParchisClase.tira_dados()

    # Verifica los valores esperados de dado1 y dado2
    assert 1<=ParchisClase.dado1 <= 6
    assert 1 <= ParchisClase.dado2 <= 6
