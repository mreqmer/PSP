from multiprocessing import *
from time import sleep


def lee_fichero(t1L):
    fichero = "C:\\Users\\porqu\\OneDrive\\Escritorio\\repo\\PSP\\Boletin01_Procesos\\ficherito\\ficherito.txt"
    with open(fichero, "r") as archivo:
        for line in archivo.readlines():
            num = int(line)
            t1L.send(num)

        t1L.send(None)


def suma_numeros(t1R):
    #que no se me olvide que la Right, que es la que recibe
    #hay que hacerle recv para que le asigne el valor a la variable deseada
    numero = t1R.recv()

    while(numero is not None):
        suma = sum(range(1, numero + 1))
        print(f"Suma hasta el {numero}: {suma}")
        sleep(1)
        numero = t1R.recv()

if __name__ == '__main__':
    t1R, t1L = Pipe()

    p1 = Process(target=lee_fichero, args=(t1L,))
    p2 = Process(target=suma_numeros, args=(t1R,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()