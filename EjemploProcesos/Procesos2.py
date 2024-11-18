from multiprocessing import Process, Queue
from random import random, randint
from time import sleep

def productor(q, id):
    for i in range(10):
        if q.full():
                print(f"P{id} La cola esta llena")
        q.put(i)
        print(f"P{id}Enviado", i)
        sleep(randint(1, 5))
    q.put(None)
    print (f" C{id}: La produccion ha acabado")

def consumidor(q, id):
    while True:
        if q.empty():
            print(f" C{id}: No hay nada en la cola")
        item = q.get()
        if item is None:
            break
        print(f" C{id}:Recibido", item)
        sleep(randint(1, 5))
    print(f" C{id}No hay mas elementos en la cola")


if __name__ == '__main__':
    productores = []
    consumidores = []
    queue = Queue(maxsize=3)
    for i in range(3):
            productores.append(Process(target = productor, args=[queue,i, ]))
            consumidores.append(Process(target = consumidor, args=[queue,i, ]))
    for i in range(3):
        productores[i].start()
    for i in range(3):
        consumidores[i].start()
    for i in range(3):
        productores[i].join()
    for i in range(3):
        consumidores[i].join()

    print("Todas las tareas se gan acabado")

