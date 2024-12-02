import os
from multiprocessing import *
from time import sleep


def suma_numeros(q, numero):
    suma = sum(range(1, numero + 1))
    pid = os.getpid()
    print(f"{pid}: Suma de los valores hasta el {numero}: {suma}")

def carga_numeros(num_max):
    numeritos = []
    for i in range(num_max+1):
        numeritos.append(i)
    return numeritos

if __name__ == '__main__':

    n = input('Hasta que número quiere las sumas?')
    numeritos = carga_numeros(int(n))
    queue = Queue(maxsize=2)

    for num in numeritos:
        p = Process(target=suma_numeros, args=(queue, num))
        p.start()
        p.join()

    print("Fiiin")





