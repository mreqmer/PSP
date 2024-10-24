from flask import Blueprint, jsonify

rutaFichero = "proyecto\\files\\asignaturas.jason"
asignaturasBP = Blueprint('asignaturas', __name__)

@asignaturasBP.get('/asignaturas')
def get_asignaturas():
    asignaturas = leeFichero()
    return jasonify(asignaturas)

@asignaturasBP.get("/asignaturas/<int:id>")
def get_asignatura(id):
    asignaturas = leeFichero()
    for asignatura in asignaturas:
        if asignatura['id'] == id:
            return asignatura, 200
    return{"error":"Asignatura not found"}, 404

