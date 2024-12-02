from multiprocessing import *



def suma_numeros(valor1, valor2):
    suma = sum(range(min(valor1, valor2), max(valor1, valor2) + 1))

    print(f"Suma de los valores entre {valor1} y {valor2}: {suma}")

if __name__ == '__main__':

    p1 = Process(target = suma_numeros, args=(1,2,))
    p2 = Process(target = suma_numeros, args=(8,2,))
    p3 = Process(target = suma_numeros, args=(3,8,))
    p4 = Process(target = suma_numeros, args=(9,20,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()