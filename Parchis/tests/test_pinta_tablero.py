import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parchis.ParchisClase import ParchisClase

#ideas de test el test1 hacer por cada bucle ir añadiendo las filas e ir probando poco a poco ya que
#cada fila corresponde a un tes

#test 2 cambiar las pos a mano  a ver si cambian bien

#test 3 cambiar pos con limites

#test 4 cambiar tamaño tableor

def test_pinta_tablero1():
    parchis = ParchisClase ("juan", "pepe")
    cadEsperada = "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    cadEsperada +="juan\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    cadEsperada += "pepe\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF"
    assert parchis.pinta_tablero(parchis) == cadEsperada

def test_pinta_tablero2():
    parchis = ParchisClase ("juan", "pepe")
    parchis.ficha_j1 = 5

    cadEsperada = "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    cadEsperada += "juan\tI\t\t\t\t\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    cadEsperada += "pepe\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF"
    assert parchis.pinta_tablero(parchis) == cadEsperada

def test_pinta_tablero3():
    parchis = ParchisClase ("juan", "pepe")
    parchis.ficha_j1=1
    parchis.ficha_j2=1
    cadEsperada = "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    cadEsperada += "juan\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    cadEsperada += "pepe\tI\tO\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF"
    assert parchis.pinta_tablero(parchis) == cadEsperada

def test_pinta_tablero4():
    parchis = ParchisClase ("juan", "pepe")
    parchis.ficha_j1=20
    parchis.ficha_j2=20
    cadEsperada = "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    cadEsperada += "juan\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tO\n"
    cadEsperada += "pepe\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tO"
    assert parchis.pinta_tablero(parchis) == cadEsperada

def test_pinta_tablero5():
    parchis = ParchisClase ("juan", "pepe")
    ParchisClase.TAM_TABLERO = 10
    cadEsperada = "\t\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\tF\n"
    cadEsperada += "juan\tI\t\t\t\t\t\t\t\t\t\tF\n"
    cadEsperada += "pepe\tI\t\t\t\t\t\t\t\t\t\tF"
    assert parchis.pinta_tablero(parchis) == cadEsperada