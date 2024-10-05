#coding: latin1

from pip._vendor import requests

apiUrl = "https://placeholder.com/"

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
Añade un profesor
"""
def nuevoProfesor(id, dni, nombre, apellidos, telefono, direccion, cuentaBancaria):
    urlNuevoProfesor = apiUrl + "profesores"
    datos = {"id":id, "dni":dni, "nombre":nombre, "apellidos":apellidos, "telefono": telefono, "direccion":direccion, "cuentaBancaria":cuentaBancaria}
    response = requests.post( urlNuevoProfesor, json=datos)

    return response

"""
Modifica Profesor
"""
def modificaProfesor(id, dni, nombre, apellidos, telefono, direccion, cuentaBancaria):
    urlModificaProfesor = apiUrl + "profesores/" + str(id)
    datos = {"id":id, "dni":dni, "nombre":nombre, "apellidos":apellidos, "telefono": telefono, "direccion":direccion, "cuentaBancaria":cuentaBancaria}
    response = str(requests.put(urlModificaProfesor, json=datos).json())
     
    return response



"""
Añade una asignatura
"""
def nuevaAsignatura(id, titulo, numHoras, idProfesor):
    urlNuevoPost = apiUrl + "asignaturas"
    datos = {"id":id, "titulo":titulo, "numHoras":numHoras, "idProfesor":idProfesor}
    response = requests.post( urlNuevoPost, json=datos)

    return response

"""
Modifica Asignatura
"""
def modificaProfesor(id, titulo, numHoras, idProfesor):
    urlModificaAsignatura = apiUrl + "Asignaturas/" + str(id)
    datos = {id, titulo, numHoras, idProfesor}
    response = str(requests.put(urlModificaAsignatura, json=datos).json())
     
    return response

"""
Elimina Profesor
"""
def eliminaProfesor(id)
    urlEliminaProfesor = apiUrl + "Profesores/" + str(id)
    response = str(requests.delete(urlEliminaProfesor).json())

    return response

"""
Elimina Asignatura
"""
def eliminaProfesor(id)
    urlEliminaAsignatura = apiUrl + "Asignaturas/" + str(id)
    response = str(requests.delete(urlEliminaAsignatura).json())

    return response















