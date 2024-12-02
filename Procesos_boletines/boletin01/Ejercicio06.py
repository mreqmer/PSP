from multiprocessing import *



def suma_numeros(valor1, valor2):
    suma = sum(range(min(valor1, valor2), max(valor1, valor2) + 1))
    print(f"Suma de los valores entre {valor1} y {valor2}: {suma}")
    return suma


if __name__ == '__main__':
    numeros = [
        {1, 2},
        {8, 2},
        {3, 8},
        {9, 20},
    ]

    with Pool(processes = 3) as pool:
        results = pool.starmap(suma_numeros, numeros)

    print("Resultados" + str(results))