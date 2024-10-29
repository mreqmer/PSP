from crud.CrudAsignaturas import *
from crud.CrudProfesores import *
from crud.CrudUsuarios import login_usuarios, usar_token


def menu():
    print("\n--- Menú ---")
    print("1. Profesores")
    print("2. Asignaturas")
    print("3. LogIn")
    print("0. Salir de la aplicación")


def Main():
    menu()
    opc = input("Selecciona una opción: ")
    while(opc!="0"):
        match opc:
            case "1":
                printMenuProfesores()
                opc = input("Selecciona una opción: ")
                menuProfesores(opc, token)
            case "2":
                printMenuAsignaturas()
                opc = input("Selecciona una opción: ")
                menuAsignaturas(opc)
            case "3":
                token = login_usuarios()
                print(token)

            case _:
                print("Opcion invalida")

        menu()
        opc = input("Selecciona una opción: ")
    print("Saliendo...")
if __name__ == '__main__':
    Main()