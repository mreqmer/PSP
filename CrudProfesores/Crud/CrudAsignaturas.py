from pip._vendor import requests

apiUrl = "http://localhost:5050/"

"""
Muestra todas las asignaturas
"""
def getAsignaturas():
    urlAsignaturas = apiUrl + "asignaturas"
    response = str(requests.get(urlAsignaturas).json())
    return response
"""
Muestra una asignatura
"""
def getAsignatura(id):
    urlAsignatura = apiUrl + "asignaturas/" + str(id)
    response = str(requests.get(urlAsignatura).json())
    return response
"""
Anade una asignatura
"""
def postAsignatura(asignatura):
    urlNuevaAsignatura = apiUrl + "asignaturas"
    response = requests.post(urlNuevaAsignatura, json=asignatura)
    return response
"""
Modifica una asignatura
"""
def putAsignatura(id, asignatura):
    urlModificaAsignatura = apiUrl + "asignaturas/" + str(id)
    response = str(requests.put(urlModificaAsignatura, json=asignatura).json())
    return response
"""
Borra una asignatura
"""
def deleteAsignatura(id):
    urlBorraAsignatura = apiUrl + "asignaturas/" + str(id)
    response = str(requests.delete(urlBorraAsignatura).json())
    return response
"""
Pregunta datos de una asignatura
"""
def datosAsignatura():
    titulo = input("Introduce el nombre: ")
    numHoras = input("Introduce el numero de horas: ")
    idProfesor = input("Introduce el id del profesor que la imparte: ")
    asignatura = {"titulo": titulo, "numHoras": numHoras, "idProfesor": idProfesor}
    return asignatura

"""
Muestra el menu para la gestion de asignaturas
"""
def printMenuAsignaturas():
    print("\n--- Menú ---")
    print("1. Mostrar asignaturas ")
    print("2. Buscar una asignatura ")
    print("3. Añadir asignatura ")
    print("4. Actualizar asignatura ")
    print("5. Eliminar asignatura")
    print("0. Salir de la aplicación")

"""
Funcionalidad del menu de las asignaturas
"""
def menuAsignaturas(opc):
    match opc:
        case "1":
            print(getAsignaturas())
        case "2":
            id = int(input("Introduce el id de la asignatura: "))
            print(getAsignatura(id))
        case "3":
            nueva_asignatura = datosAsignatura()
            print(postAsignatura(nueva_asignatura))
        case "4":
            id = int(input("Introduce el id de la asignatura a modificar: "))
            actualiza_asignatura = datosAsignatura()
            print(putAsignatura(id, actualiza_asignatura))
        case "5":
            id = int(input("Introduce el id de la asignatura a borrar: "))
            print(deleteAsignatura(id))
        case _:
            print("Opcion invalida")
