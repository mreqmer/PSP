from ApiRest.Crud import mostrarAsignaturas, nuevoProfesor, modificaProfesor
from Crud import mostrarProfesores

"""
Muestra un menú con las opciones
"""
def menu():
    print("\n--- Menú ---")
    print("1. Mostrar profesores")
    print("2. Mostrar asignaturas")
    print("3. Añadir profesor")
    print("4. Actualizar profesor")
    print("5. Añadir asignatura")
    print("6. Modificar asignatura")
    print("7. Eliminar profesor")
    print("8. Eliminar Asignatura")
    print("0. Salir de la aplicación")

def Main():

    menu()
    opc = -1
    opc = input("Selecciona una opción: ")
    while(opc!=0):
        match opc:
            case "1":
                print(opc)
                print(mostrarProfesores())
            case "2":
                print(opc)
                mostrarAsignaturas()
            case "3":
                print(opc)
                nuevoProfesor("1234AB", "Paco", "Paquito", "999888777", "qweqwe", "ghfh")
            case "4":
                print(opc)
                modificaProfesor(4, "1234AB", "Paco", "Mariano", "999888777", "qweqwe", "ghfh")
            case "5":
                ...
            case "6":
                ...
            case "7":
                ...
            case "8":
                ...
            case "9":
                ...
            case "0":
                print("Saliendo.")
        menu()
        opc = input("Selecciona una opción: ")

if __name__ == '__main__':
    Main()