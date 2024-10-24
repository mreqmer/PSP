import json

def leeFichero(ruta):
    archivo = open(ruta, "r")
    res = json.load(archivo)
    archivo.close()
    return res

def escribeFichero(ruta, cosas):
    archivo = open(ruta, "w")
    json.dump(cosas, archivo)
    archivo.close()