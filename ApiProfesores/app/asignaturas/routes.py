from flask import Blueprint, jsonify, request

from app.ficheros.leer_escribir import leeFichero, escribeFichero

rutaAsignaturas = "app/ficheros/asignaturas.json"
asignaturasBP = Blueprint('asignaturas', __name__)

@asignaturasBP.get('/')
def get_asignaturas():
    asignaturas = leeFichero(rutaAsignaturas)
    return jsonify(asignaturas)

@asignaturasBP.get("/<int:id>")
def get_asignatura(id):
    asignaturas = leeFichero(rutaAsignaturas)
    for asignatura in asignaturas:
        if asignatura['id'] == id:
            return asignatura, 200
    return{"error":"Asignatura not found"}, 404

@asignaturasBP.post('/')
def nueva_asignatura():
    if request.json:
        asignaturas = leeFichero(rutaAsignaturas)
        asignatura = request.get_json()
        asignatura["id"] = findNextIdAsignatura()
        asignaturas.append(asignatura)
        escribeFichero(rutaAsignaturas, asignaturas)
        return asignatura, 201
    return {"error": "Request must be JSON"}, 404


@asignaturasBP.put('/<int:id>')
@asignaturasBP.patch('/<int:id>')
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

@asignaturasBP.delete('/<int:id>')
def eliminar_asignatura(id):
    asignaturas = leeFichero(rutaAsignaturas)
    for asignatura in asignaturas:
        if asignatura['id'] == id:
            asignaturas.remove(asignatura)
            escribeFichero(rutaAsignaturas, asignaturas)
            return {}, 200
    return {"error": "Asignatura not found"}, 404

def findNextIdAsignatura():
    asignaturas = leeFichero(rutaAsignaturas)
    return max(asignatura["id"] for asignatura in asignaturas) + 1