#coding: latin1

from pip._vendor import requests

apiUrl = "https://jsonplaceholder.typicode.com/"

"""
Muestra un men� con las opciones
"""
def menu():
    print("\n--- Men� ---")
    print("1. Mostrar todas las publicaciones")
    print("2. Mostrar una publicaci�n concreta")
    print("3. A�adir una nueva publicaci�n")
    print("4. Modificar todos los datos de una publicaci�n")
    print("5. Modificar un dato concreto de una publicaci�n")
    print("6. Eliminar una publicaci�n")
    print("7. Salir de la aplicaci�n")

"""
Muestra todas las publicaciones de los usuarios
"""
def mostrarPublicaciones():
    
    urlPosts = apiUrl + "posts"
    response = str(requests.get(urlPosts).json())
    
    return response

"""
Muestra las publicaciones de un usuario en concreto
"""
def mostrarPublicacionesUsuario(id):

    urlPostsUsuario = apiUrl + "posts/" + str(id)
    response = str(requests.get(urlPostsUsuario).json())

    return response

"""
A�ade una nueva publicaci�n a un usuario
"""
def nuevaPublicacion(id, titulo, publicacion):
    urlNuevoPost = apiUrl + "posts"
    datos = {"userId":1, "id": id, "title":titulo, "body":publicacion}
    response = requests.post( urlNuevoPost, json=datos)

    return response

"""
Modifica una publicaci�n de un usuario
"""
def modificaPublicacion(id, titulo, publicacion):
    urlModificaPost = apiUrl + "posts/" + id
     

print(str(nuevaPublicacion(1, "hola", "cosa de escribir")))