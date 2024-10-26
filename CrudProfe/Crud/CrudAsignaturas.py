from pip._vendor import requests

from Crud.Asignatura import Asignatura

apiUrl = "http://127.0.0.1:5000/"


"""
Muestra todas las asignaturas
"""
def getAsignaturas():
    id = input("Introduce el id: ")
    urlAsignaturas = apiUrl + "asignaturas/" + str(id)
    response = str(requests.get(urlAsignaturas).json())
    return response

"""
Anade una asignatura
"""

def postAsignatura(asignatura):
    urlNuevaAsignatura = apiUrl + "asignaturas"
    datos = vars(asignatura)
    response = requests.post(urlNuevaAsignatura, json=datos)
    return response

"""
Modifica Asignatura
"""

def putAsginatura(asignatura):
    datos = vars(asignatura)
    id = datos.get("id")
    urlModificaAsignatura = apiUrl + "asignaturas/" + str(id)
    response = str(requests.put(urlModificaAsignatura, json=datos).json())

    return response

"""
Elimina Asignatura
"""
def deleteAsignatura(asignatura):
    datos = vars(asignatura)
    id = datos.get("id")
    urlEliminaAsignatura = apiUrl + "asignaturas/" + str(id)
    response = str(requests.delete(urlEliminaAsignatura).json())
    return response


"""
Pregunta datos de una asignatura nueva
"""
def datosAddAsignatura():
    id = 0
    titulo = input("Introduce el titulo: ")
    numHoras = input("Introduce el numero de horas: ")
    idProfesor = input("Introduce el id de profesor: ")
    return Asignatura(id, titulo, numHoras, idProfesor)

"""
Pregunta datos para modificar una asignatura
"""
def datosModificaAsignatura():
    id = int(input("Introduce el id de la asignatura a modificar: "))
    titulo = input("Introduce el nuevo titulo: ")
    numHoras = input("Introduce el numero numero de horas: ")
    idProfesor = input("Introduce el nuevo id de profesor: ")
    return Asignatura(int(id), titulo, numHoras, idProfesor)
"""
Pregunta datos para borrar una asignatura
"""
def datosDeleteAsignatura():
    id = input("Introduce el id de la asignatura a borrar: ")
    titulo = 0
    numHoras = 0
    idProfesor = 0

    return Asignatura(int(id), titulo,numHoras, idProfesor)