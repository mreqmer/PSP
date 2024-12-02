from multiprocessing import *
import time

def carga_numeros(numero_suma):
    array_suma = []
    for i in range (1, numero_suma+1):
        array_suma.append(i+1)
    return array_suma


def suma_numeros(numero):
    suma = 0
    for i in range(1, numero):
        suma+=i
    return suma

if __name__ == '__main__':

    n = input('Hasta que número quiere las sumas?')

    sumas = carga_numeros(int(n))

    with Pool(processes = 3) as pool:
        results = pool.map(suma_numeros, sumas)

    print("Resultados: ", results)