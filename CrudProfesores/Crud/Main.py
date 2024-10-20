
from Crud.CrudAsignaturas import *
from Crud.CrudProfesores import *

"""
Muestra un menú con las opciones
"""
def menu():
    print("\n--- Menú ---")
    print("1. Mostrar profesores")
    print("2. Añadir profesor")
    print("3. Actualizar profesor")
    print("4. Eliminar profesor")
    print("------------------------")
    print("5. Mostrar asignaturas  ")
    print("6. Añadir asignatura ")
    print("7. Actualizar asignatura ")
    print("8. Eliminar asignatura")
    print("0. Salir de la aplicación")


def Main():

    menu()
    opc = -1
    opc = input("Selecciona una opción: ")
    while(opc!=0):
        match opc:
            case "1":
                print(getProfesores())
            case "2":
                nuevoProfesor = datosAddProfesor()
                postProfesor(nuevoProfesor)
            case "3":
                nuevoProfesor = datosModificaProfesor()
                putProfesor(nuevoProfesor)
            case "4":
                nuevoProfesor = datosDeleteProfesor()
                deleteProfesor(nuevoProfesor)
            case "5":
                print(getAsignaturas())
            case "6":
                nuevaAsignatura = datosAddAsignatura()
                postAsignatura(nuevaAsignatura)
            case "7":
                nuevaAsignatura = datosModificaAsignatura()
                putAsginatura(nuevaAsignatura)
            case "8":
                nuevaAsignatura = datosDeleteAsignatura()
                deleteAsignatura(nuevaAsignatura)
            case "0":
                print("Saliendo.")
        menu()
        opc = input("Selecciona una opción: ")

if __name__ == '__main__':
    Main()