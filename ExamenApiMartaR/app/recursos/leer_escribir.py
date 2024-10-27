import json

"""
Lee un fichero donde estan contenido los datos de la api
"""
def leeFichero(ruta):
    archivo = open(ruta, "r")
    res = json.load(archivo)
    archivo.close()
    return res
"""
Escribe un fichero donde estan contenido los datos de la api
"""
def escribeFichero(ruta, cosas):
    archivo = open(ruta, "w")
    json.dump(cosas, archivo)
    archivo.close()