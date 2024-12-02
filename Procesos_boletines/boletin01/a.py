from multiprocessing import *


def incrementar(id, valor, lock):
    for i in range(10000):
        with lock:
            print(f"P{id} incrementa el valor {valor.value}")
            valor.value+=1

if __name__ == "__main__":
    contador = Value("i", 0)
    lock = Lock()
    procesos = [Process(target = incrementar, args=(id, contador, lock,)) for _ in range(4)]



    for p in procesos:

        p.start()

    for p in procesos:
            p.join()

    print(f"Resultado: {contador.value}")