from crud.CrudAsignaturas import *
from crud.CrudProfesores import *

def menu():
    print("\n--- Menú ---")
    print("1. Profesores")
    print("2. Asignaturas")
    print("0. Salir de la aplicación")


def Main():
    menu()
    opc = input("Selecciona una opción: ")
    while(opc!="0"):
        match opc:
            case "1":
                printMenuProfesores()
                opc = input("Selecciona una opción: ")
                menuProfesores(opc)
            case "2":
                printMenuAsignaturas()
                opc = input("Selecciona una opción: ")
                menuAsignaturas(opc)
            case _:
                print("Opcion invalida")

        menu()
        opc = input("Selecciona una opción: ")
    print("Saliendo...")
if __name__ == '__main__':
    Main()