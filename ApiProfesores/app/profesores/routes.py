from flask import Blueprint, jsonify, request
from app.ficheros.leer_escribir import leeFichero, escribeFichero

profesoresBP = Blueprint('profesores', __name__)
rutaProfesores = "app/ficheros/profesores.json"
rutaAsignaturas = "app/ficheros/asignaturas.json"

@profesoresBP.get('/')
def get_profesores():
    profesores = leeFichero(rutaProfesores)
    return jsonify(profesores)

@profesoresBP.get("/<int:id>")
def get_profesor(id):
    profesores = leeFichero(rutaProfesores)
    for profesor in profesores:
        if profesor['id'] == id:
            return profesor, 200
    return{"error":"Profesor not found"}, 404


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



@profesoresBP.post("/")
def add_profesores():
    profesores  = leeFichero(rutaProfesores)
    if request.is_json:
        profesor = request.get_json()
        profesor['id'] = findNextId()
        profesores.append(profesor)
        escribeFichero("profesores.json", profesores)



"""
Busca el siguiente id de una asignatura
"""
def findNextId():
    profesores = leeFichero("profesores.json")
    return max(profesor["id"] for profesor in profesores) + 1