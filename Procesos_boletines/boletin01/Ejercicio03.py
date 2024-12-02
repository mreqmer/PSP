
from multiprocessing import Queue, Process

def lee_fichero(cola: Queue):
    fichero = "C:\\Users\\porqu\\OneDrive\\Escritorio\\repo\\PSP\\Boletin01_Procesos\\ficherito\\ficherito.txt"
    with open(fichero, "r") as archivo:
        for line in archivo.readlines():
            num = int(line)
            cola.put(num)

        cola.put(None)

def suma_numeros(numero):
    return sum(range(1, numero + 1))

def suma_cola(cola: Queue):
    numero = cola.get()
    suma = 0
    while numero is not None:
        suma = suma_numeros(numero)
        print(f"Suma hasta el {numero}: {suma}")
        numero = cola.get()

        suma = 0

if __name__ == '__main__':

    queue = Queue()

    p1 = Process(target=lee_fichero, args=(queue,))
    p2 = Process(target=suma_cola, args=(queue,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()