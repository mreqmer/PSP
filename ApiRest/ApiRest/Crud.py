
from pip._vendor import requests

apiUrl = "http://127.0.0.1:5000/"



"""
Muestra todos los profesores
"""
def mostrarProfesores():
    
    urlProfesores = apiUrl + "profesores"
    response = str(requests.get(urlProfesores).json())
    
    return response


"""
Muestra todas las asignaturas
"""
def mostrarAsignaturas():
    
    urlAsignaturas = apiUrl + "asignaturas"
    response = str(requests.get(urlAsignaturas).json())
    
    return response

"""
Anade un profesor
"""

def nuevoProfesor(dni, nombre, apellidos, telefono, direccion, cuentaBancaria):
    urlNuevoProfesor = apiUrl + "profesores"
    datos = {"dni":dni, "nombre":nombre, "apellidos":apellidos, "telefono": telefono, "direccion":direccion, "cuentaBancaria":cuentaBancaria}
    response = requests.post( urlNuevoProfesor, json=datos)

    return response

"""
Modifica Profesor
"""
def modificaProfesor(id, dni, nombre, apellidos, telefono, direccion, cuentaBancaria):
    urlModificaProfesor = apiUrl + "profesores/" + str(id)
    datos = {"dni":dni, "nombre":nombre, "apellidos":apellidos, "telefono": telefono, "direccion":direccion, "cuentaBancaria":cuentaBancaria}
    response = str(requests.put(urlModificaProfesor, json=datos).json())
     
    return response




#Añade una asignatura

def nuevaAsignatura(id, titulo, numHoras, idProfesor):
    urlNuevoPost = apiUrl + "asignaturas"
    datos = {"id":id, "titulo":titulo, "numHoras":numHoras, "idProfesor":idProfesor}
    response = requests.post( urlNuevoPost, json=datos)

    return response

"""
Modifica Asignatura
"""
def modificaAsginatura(id, titulo, numHoras, idProfesor):
    urlModificaAsignatura = apiUrl + "Asignaturas/" + str(id)
    datos = {id, titulo, numHoras, idProfesor}
    response = str(requests.put(urlModificaAsignatura, json=datos).json())
     
    return response

"""
Elimina Profesor
"""
def eliminaProfesor(id):
    urlEliminaProfesor = apiUrl + "Profesores/" + str(id)
    response = str(requests.delete(urlEliminaProfesor).json())

    return response

"""
Elimina Asignatura
"""
def eliminaProfesor(id):
    urlEliminaAsignatura = apiUrl + "Asignaturas/" + str(id)
    response = str(requests.delete(urlEliminaAsignatura).json())

    return response















