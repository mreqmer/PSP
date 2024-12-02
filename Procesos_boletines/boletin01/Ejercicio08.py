from multiprocessing import *


def lee_fichero(pipeLeft):
    fichero = "C:\\Users\\porqu\\OneDrive\\Escritorio\\repo\\PSP\\Boletin01_Procesos\\ficherito\\fichero_multiple.txt"
    with open(fichero, "r") as archivo:
        for line in archivo.readlines():
            numeros = line.strip()
            pipeLeft.send(numeros)

        pipeLeft.send(None)

def suma_numeros(pipeRight):
    valores = pipeRight.recv()

    while valores is not None:
        valor_separado = valores.split()
        valor1 = int(valor_separado[0])
        valor2 = int(valor_separado[1])
        suma = sum(range(min(valor1, valor2), max(valor1, valor2) + 1))
        print(f"Suma de los valores entre {valor1} y {valor2}: {suma}")
        valores = pipeRight.recv()

if __name__ == '__main__':

    pipeLeft, pipeRight = Pipe()

    p1 = Process(target=lee_fichero, args=(pipeLeft,))
    p2 = Process(target=suma_numeros, args=(pipeRight,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
