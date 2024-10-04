#coding: latin1

from pip._vendor import requests

apiUrl = "https://placeholder.com/"

"""
Muestra un men� con las opciones
"""
def menu():
    print("\n--- Men� ---")
    print("1. Mostrar profesores")
    print("2. Mostrar asignaturas")
    print("3. A�adir profesor")
    print("4. Actualizar profesor")
    print("5. A�adir asignatura")
    print("6. Modificar asignatura")
    print("7. Eliminar profesor")
    print("8. Eliminar Asignatura")
    print("0. Salir de la aplicaci�n")

"""
Muestra todos los profesores
"""
def mostrarProfesores():
    
    urlPosts = apiUrl + "profesores"
    response = str(requests.get(urlPosts).json())
    
    return response


"""
Muestra todas las asignaturas
"""
def mostrarAsignaturas():
    
    urlPosts = apiUrl + "asignaturas"
    response = str(requests.get(urlPosts).json())
    
    return response

"""
A�ade un profesor
"""
def nuevoProfesor(id, dni, nombre, apellidos, telefono, direccion, cuentaBancaria):
    urlNuevoPost = apiUrl + "profesores"
    datos = {"id":id, "dni":dni, "nombre":nombre, "apellidos":apellidos, "telefono": telefono, "direccion":direccion, "cuentaBancaria":cuentaBancaria}
    response = requests.post( urlNuevoPost, json=datos)

    return response

"""
Modifica Profesor
"""
def modificaProfesor(id, dni, nombre, apellidos, telefono, direccion, cuentaBancaria):
   urlModificaProfesor = apiUrl + "profesores/" + str(id)
    datos = {"id":id, "dni":dni, "nombre":nombre, "apellidos":apellidos, "telefono": telefono, "direccion":direccion, "cuentaBancaria":cuentaBancaria}
    response = str(requests.put(urlModificaPost, json=datos).json())
     
    return response


"""
A�ade una asignatura
"""
def nuevaAsignatura(id, titulo, numHoras, idProfesor):
    urlNuevoPost = apiUrl + "asignaturas"
    datos = {"id":id, "titulo":titulo, "numHoras":numHoras, "idProfesor":idProfesor}
    response = requests.post( urlNuevoPost, json=datos)

    return response







