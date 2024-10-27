from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.utils.leer_escribir import leeFichero, escribeFichero


profesoresBP = Blueprint('profesores', __name__)
#Ruta del fichero donde estan los JSON de los profesores
rutaProfesores = "app/ficheros/profesores.json"
#Ruta del fichero donde estan los JSON de asignaturas
rutaAsignaturas = "app/ficheros/asignaturas.json"

"""
Obtiene los profesores del fichero
"""
@profesoresBP.get('/')
def get_profesores():
    profesores = leeFichero(rutaProfesores)
    return jsonify(profesores)

"""
Obtiene un profesor en concreto del fichero
"""
@profesoresBP.get("/<int:id>")
def get_profesor(id):
    profesores = leeFichero(rutaProfesores)
    for profesor in profesores:
        if profesor['id'] == id:
            return profesor, 200
    return{"error":"Profesor not found"}, 404

"""
Obtiene las asignaturas que imparte un profesor en concreto
"""
@profesoresBP.get("/<int:id>/asignaturas")
def get_profesor_asignaturas(id):
    list = []
    asignaturas = leeFichero(rutaAsignaturas)
    for asignatura in asignaturas:
        if asignatura['idProfesor'] == id:
            list.append(asignatura)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "no Asignaturas for this Profesor"}, 404

"""
Crea una nuevo profesor y lo anade al fichero
"""
@profesoresBP.post("/")
@jwt_required()
def add_profesores():
    if request.is_json:
        profesores = leeFichero(rutaProfesores)
        profesor = request.get_json()
        profesor["id"] = findNextId()
        profesores.append(profesor)
        escribeFichero(rutaProfesores, profesores)
        return profesor, 201
    return {"error": "Request must be JSON"}, 404

"""
Modifica uno o varios elementos de un objeto y lo anade al fichero
"""
@profesoresBP.put("/<int:id>")
@profesoresBP.patch("/<int:id>")
@jwt_required()
def modfica_profesores(id):
    if request.is_json:
        profesores = leeFichero(rutaProfesores)
        nuevoProfesor = request.get_json()
        for profesor in profesores:
            if profesor['id'] == id:
                for element in nuevoProfesor:
                    profesor[element] = nuevoProfesor[element]
                escribeFichero(rutaProfesores, profesores)
                return profesor, 200
    return {"error":"Request must be JSON"}, 404

"""
Borra un profesor
"""

@profesoresBP.delete("/<int:id>")
@jwt_required()
def delete_profesores(id):
    profesores = leeFichero(rutaProfesores)
    for profesor in profesores:
        if profesor['id'] == id:
            profesores.remove(profesor)
            escribeFichero(rutaProfesores, profesores)
            return {}, 200
    return {"error": "Profesor not found"}, 404



"""
Busca el siguiente id que puede tener un profesor
"""
def findNextId():
    profesores = leeFichero(rutaProfesores)
    return max(profesor["id"] for profesor in profesores) + 1