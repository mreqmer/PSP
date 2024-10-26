from pip._vendor import requests

from Crud.Profesor import Profesor

apiUrl = "http://127.0.0.1:5000/"


"""
Muestra todos los profesores
"""
def getProfesores():
    id = input("Introduce el id: ")
    urlProfesores = apiUrl + "profesores/" + str(id)
    response = str(requests.get(urlProfesores).json())
    return response

"""
Anade un profesor
"""
def postProfesor(profesor):
    urlNuevoProfesor = apiUrl + "profesores"
    datos = vars(profesor)
    response = requests.post(urlNuevoProfesor, json=datos)
    return response

"""
Modifica Profesor
"""
def putProfesor(profesor):
    datos = vars(profesor)
    id = datos.get("id")
    urlModificaProfesor = apiUrl + "profesores/" + str(id)
    response = str(requests.put(urlModificaProfesor, json=datos).json())

    return response


"""
Elimina Profesor
"""
def deleteProfesor(profesor):
    datos = vars(profesor)
    id = datos.get("id")
    urlEliminaProfesor = apiUrl + "profesores/" + str(id)
    response = str(requests.delete(urlEliminaProfesor).json())

    return response

"""
Pregunta datos de un profesor nuevo
"""
def datosAddProfesor():
    id = 0
    nombre = input("Introduce el nombre: ")
    apellidos = input("Introduce el apellidos: ")
    telefono = input("Introduce el telefono: ")
    direccion = input("Introduce el direccion: ")
    cc = input("Introduce el Cuenta Bancaria: ")
    return Profesor( id, nombre, apellidos, telefono, direccion, cc)

"""
Pregunta datos para modificar un profesor
"""
def datosModificaProfesor():
    id = int(input("Introduce el id del profesor a modificar: "))
    nombre = input("Introduce el nuevo nombre: ")
    apellidos = input("Introduce el nuevo apellidos: ")
    telefono = input("Introduce el nuevo telefono: ")
    direccion = input("Introduce la nueva direccion: ")
    cc = input("Introduce el nueva Cuenta Bancaria: ")
    return Profesor(int(id), nombre, apellidos, telefono, direccion, cc)
"""
Pregunta datos para borrar un profesor
"""
def datosDeleteProfesor():
    id = input("Introduce el id del profesor a borrar: ")
    nombre = 0
    apellidos = 0
    telefono = 0
    direccion = 0
    cc = 0

    return Profesor(int(id), nombre,apellidos, telefono, direccion, cc)