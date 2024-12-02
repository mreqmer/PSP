
from multiprocessing import *


def lee_fichero(cola : Queue):
    fichero = "C:\\Users\\porqu\\OneDrive\\Escritorio\\repo\\PSP\\Boletin01_Procesos\\ficherito\\fichero_multiple.txt"
    with open(fichero, "r") as archivo:
        for line in archivo.readlines():
            numeros = line.strip()

            cola.put(numeros)
        cola.put(None)


def suma_numeros(cola: Queue):

    valores = cola.get()

    while valores != None:
        valor_separado = valores.split()
        valor1 = int(valor_separado[0])
        valor2 = int(valor_separado[1])
        suma = sum(range(min(valor1, valor2), max(valor1, valor2) + 1))
        print(f"Suma de los valores entre {valor1} y {valor2}: {suma}")
        valores = cola.get()

if __name__ == '__main__':

    queue = Queue()
    p1 = Process(target=lee_fichero, args=(queue,))
    p2= Process(target=suma_numeros, args=(queue,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()