from pip._vendor import requests

apiUrl = "http://127.0.0.1:5000/"

"""
Muestra todos los profesores
"""
def getProfesores():
    urlProfesores = apiUrl + "profesores"
    response = str(requests.get(urlProfesores).json())
    return response
"""
Muestra un profesor
"""
def getProfesor(id):
    urlProfesores = apiUrl + "profesores/" + str(id)
    response = str(requests.get(urlProfesores).json())
    return response
"""
Muestra las asignaturas que imparte un profesor
"""
def getProfesorAsignaturas(id):
    urlProfesores = apiUrl + "profesores/" + str(id) + "/asignaturas"
    response = str(requests.get(urlProfesores).json())
    return response

"""
Anade un nuevo profesor
"""
def postProfesor(profesor):
    urlNuevoProfesor = apiUrl + "profesores"
    response = requests.post(urlNuevoProfesor, json=profesor)
    return response

"""
Modifica un profesor
"""
def putProfesor(id, profesor):
    urlModificaProfesor = apiUrl + "profesores/" + str(id)
    response = str(requests.put(urlModificaProfesor, json=profesor).json())
    return response

"""
Borra a un profesor
"""
def deleteProfesor(id):
    urlBorraProfesor = apiUrl + "profesores/" + str(id)
    response = str(requests.delete(urlBorraProfesor).json())
    return response

"""
Pregunta datos de un profesor nuevo
"""
def datosProfesor():
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce el apellidos: ")
    telefono = input("Introduce el telefono: ")
    direccion = input("Introduce el direccion: ")
    cc = input("Introduce el Cuenta Bancaria: ")
    profesor = {"nombre": nombre, "apellidos": apellidos, "telefono": telefono, "direccion": direccion,"cc": cc}
    return profesor

"""
Muestra el menu para la gestion de profesores
"""
def printMenuProfesores():
    print("\n--- Menú ---")
    print("1. Mostrar profesores")
    print("2. Buscar un profesor")
    print("3. Mostrar asignaturas de un profesor")
    print("4. Añadir profesor")
    print("5. Actualizar profesor")
    print("6. Eliminar profesor")
    print("0. Salir de la aplicación")

"""
funcionalidad del menu de los profesores
"""
def menuProfesores(opc):
    match opc:
        case "1":
            print(getProfesores())
        case "2":
            id = int(input("Introduce el id del profesor a buscar: "))
            print(getProfesor(id))
        case "3":
            id = int(input("Introduce el id del profesor: "))
            print(getProfesorAsignaturas(id))
        case "4":
            nuevo_profesor = datosProfesor()
            print(postProfesor(nuevo_profesor))
        case "5":
            id = int(input("Introduce el id del profesor a actualizar: "))
            actualiza_profesor = datosProfesor()
            print(putProfesor(id, actualiza_profesor))
        case "6":
            id = int(input("Introduce el id del profesor a borrar: "))
            print(deleteProfesor(id))
        case _:
            print("Opcion invalida")