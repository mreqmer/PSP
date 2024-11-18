from multiprocessing import Process, Pipe
from random import randint


def bombo(pipe):
    lista=[]
    while True:
        if(pipe.recv() == 0 ):
            numero = randint(1, 100)
            while numero in lista:
                numero = randint(1, 100)
            lista.append(numero)
            print(f"Numero: {numero}")
            pipe.send(numero)
        else:
            pipe.close()
            break

def jugador(pipe):
    creditos = 10
    apuesta = randint(1, 100)
    print(f"Apuesto por el {apuesta}")
    while creditos >0:
        pipe.send(0)
        creditos-=1
        numero = pipe.recv()
        if numero == apuesta:
            print("Let's gooooo")
            pipe.send(1)
            return
        else:
            print("Diablo papadio")
    print("Oh no estoy pobre")
    pipe.close()

if __name__ == '__main__':
    pipe1, pipe2 = Pipe()
    p1 = Process(target=bombo, args=(pipe1,))
    p2 = Process(target=jugador, args=(pipe2,))
    p1.start()
    p2.start()



