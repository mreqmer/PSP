#coding: latin1

from pip._vendor import requests

apiUrl = "https://jsonplaceholder.typicode.com/"

"""
Muestra un menú con las opciones
"""
def menu():
    print("\n--- Menú ---")
    print("1. Mostrar todas las publicaciones")
    print("2. Mostrar una publicación concreta")
    print("3. Añadir una nueva publicación")
    print("4. Modificar todos los datos de una publicación")
    print("5. Modificar un dato concreto de una publicación")
    print("6. Eliminar una publicación")
    print("7. Salir de la aplicación")

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
Añade una nueva publicación a un usuario
"""
def nuevaPublicacion(id, titulo, publicacion):
    urlNuevoPost = apiUrl + "posts"
    datos = {"userId":1, "id": id, "title":titulo, "body":publicacion}
    response = requests.post( urlNuevoPost, json=datos)

    return response

"""
Modifica una publicación de un usuario
"""
def modificaPublicacion(id, titulo, publicacion):
    urlModificaPost = apiUrl + "posts/" + id
     

print(str(nuevaPublicacion(1, "hola", "cosa de escribir")))