import os
from multiprocessing import *
import time
from time import sleep


def suma_numeros(numero):
    suma = sum(range(1, numero + 1))
    pid = os.getpid()
    print(f"{pid}: Suma de los valores hasta el {numero}: {suma}")


if __name__ == '__main__':

    n = input('Hasta que número quiere las sumas?')
    procesos = []

    for i in range(1, int(n) + 1):
        p = Process(target=suma_numeros, args=(i,))
        procesos.append(p)  # Agregar el proceso a la lista
        p.start()
        sleep(2)

    for p in procesos:
        p.join()


    print("Fiiin")





