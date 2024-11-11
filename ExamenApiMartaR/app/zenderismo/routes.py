from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.recursos.leer_escribir import leeFichero, escribeFichero

import app.recursos.leer_escribir

#Ruta del fichero donde estan los JSON
rutaFichero = "app/ficheros/rutas.json"

rutasBP = Blueprint('rutas', __name__)



"""
Obtiene las rutas del fichero
"""
@rutasBP.get('/')
@jwt_required()
def get_rutas():
    rutas = leeFichero(rutaFichero)
    return jsonify(rutas)

"""
Permite obtener una ruta
"""
@rutasBP.get("/<int:id>")
@jwt_required()
def get_ruta(id):
    rutas = leeFichero(rutaFichero)
    for ruta in rutas:
        if ruta['id'] == id:
            return ruta, 200
    return {"error": "Ruta not found"}, 404

"""
Crea una nueva ruta
"""
@rutasBP.post("/")
@jwt_required()
def add_ruta():
    if request.is_json:
        rutas = leeFichero(rutaFichero)
        ruta = request.get_json()
        ruta["id"] = findNextId()
        rutas.append(ruta)
        escribeFichero(rutaFichero, rutas)
        return ruta, 201
    return {"error": "Request must be JSON"}, 404

@rutasBP.put("/<int:id>")
@rutasBP.patch("/<int:id>")
@jwt_required()
def modifica_atributo_ruta(id):
    if request.is_json:
        rutas = leeFichero(rutaFichero)
        nuevaRuta = request.get_json()
        for ruta in rutas:
            if ruta['id'] == id:
                for element in nuevaRuta:
                    if element != 'id':
                        ruta[element] = nuevaRuta[element]
                escribeFichero(rutaFichero, rutas)
                return ruta, 200
    return {"error":"Request must be JSON"}, 415


@rutasBP.delete("/<int:id>")
@jwt_required()
def delete_ruta(id):
    rutas = leeFichero(rutaFichero)
    for ruta in rutas:
        if ruta['id'] == id:
            rutas.remove(ruta)
            escribeFichero(rutaFichero, rutas)
            return {}, 200
    return {"error": "Ruta not found"}, 404





"""
Busca el siguiente id que puede tener una ruta
"""
def findNextId():
    rutas = leeFichero(rutaFichero)
    return max(ruta["id"] for ruta in rutas) + 1