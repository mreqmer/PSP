from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.utils.leer_escribir import leeFichero, escribeFichero

#Ruta del fichero donde estan los JSON de asignaturas
rutaAsignaturas = "app/ficheros/asignaturas.json"

asignaturasBP = Blueprint('asignaturas', __name__)

"""
Obtiene las asignaturas del fichero
"""
@asignaturasBP.get('/')
def get_asignaturas():
    asignaturas = leeFichero(rutaAsignaturas)
    return jsonify(asignaturas)

"""
Obtiene una asignatura en concreto del fichero
"""
@asignaturasBP.get("/<int:id>")
def get_asignatura(id):
    asignaturas = leeFichero(rutaAsignaturas)
    for asignatura in asignaturas:
        if asignatura['id'] == id:
            return asignatura, 200
    return{"error":"Asignatura not found"}, 404

"""
Crea una nueva asignatura y la anade al fichero
"""
@asignaturasBP.post('/')
@jwt_required()
def nueva_asignatura():
    if request.json:
        asignaturas = leeFichero(rutaAsignaturas)
        asignatura = request.get_json()
        asignatura["id"] = findNextIdAsignatura()
        asignaturas.append(asignatura)
        escribeFichero(rutaAsignaturas, asignaturas)
        return asignatura, 201
    return {"error": "Request must be JSON"}, 404

"""
Modifica uno o varios elementos de un objeto y lo anade al fichero
"""
@asignaturasBP.put('/<int:id>')
@asignaturasBP.patch('/<int:id>')
@jwt_required()
def modificar_asignatura(id):
    if request.json:
        asignaturas = leeFichero(rutaAsignaturas)
        nuevaAsignatura = request.get_json()
        for asignatura in asignaturas:
            if asignatura['id'] == id:
                for element in nuevaAsignatura:
                    asignatura[element] = nuevaAsignatura[element]
                escribeFichero(rutaAsignaturas, asignaturas)
                return asignatura, 200
    return {"error": "Request must be JSON"}, 404

"""
Borra una asignatura
"""
@asignaturasBP.delete('/<int:id>')
@jwt_required()
def eliminar_asignatura(id):
    asignaturas = leeFichero(rutaAsignaturas)
    for asignatura in asignaturas:
        if asignatura['id'] == id:
            asignaturas.remove(asignatura)
            escribeFichero(rutaAsignaturas, asignaturas)
            return {}, 200
    return {"error": "Asignatura not found"}, 404

"""
Busca el siguiente id que puede tener una asignatura
"""
def findNextIdAsignatura():
    asignaturas = leeFichero(rutaAsignaturas)
    return max(asignatura["id"] for asignatura in asignaturas) + 1