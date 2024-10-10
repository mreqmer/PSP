#coding: latin1

from flask import *

app = Flask(__name__)

profesores = [
    {"id": 1, "nombre":"Juan", "apellidos":"Barrena","telefono":"666555444", "direccion":"C/calle bonita", "cc":"ES1234"},
    {"id": 2, "nombre":"Maria", "apellidos":"Buenavilla","telefono":"666555444", "direccion":"C/calle bonita", "cc":"ES4321"},
    {"id": 3, "nombre":"Pedro", "apellidos":"Mapache","telefono":"666555444", "direccion":"C/calle bonita", "cc":"ES5555"},
]

asignaturas = [
    {"id": 1, "titulo":"Programacion", "numHoras": "60", "idProfesor":"1"},
    {"id": 2, "titulo":"Empresa", "numHoras": "20", "idProfesor":"2"},
    {"id": 3, "titulo":"Base de datos", "numHoras": "45", "idProfesor":"1"},
    {"id": 4, "titulo":"Html", "numHoras": "50", "idProfesor":"3"},
    {"id": 5, "titulo":"Sistemas", "numHoras": "30", "idProfesor":"3"},

]

@app.route('/')
def index():
    return 'Hola a todos! :)'

"""
Métodos get para los profesores
"""
@app.get("/profesores")

def get_profesores():
    return jsonify(profesores)

@app.get("/profesores/<int:id>")

def get_country(id):
    for profesor in profesores:
        if profesor["id"] == id:
            return profesor, 200
        else:
            return {"error":"Country not found"}, 404

"""
Métodos get para las asignaturas
"""
@app.get("/asignaturas")
def get_asignaturas():
    return jsonify(asignaturas)

@app.get("/asignaturas/<int:id>")
def get_asignatura(id):
    return "A"


"""
Busca el siguiente id de un profesor
"""
def findNextId():
    return max(profesor["id"] for profesor in profesores) + 1

@app.post("/profesores")

def add_profesor():
    if request.is_json:
        profesor = request.get_json()
        profesor["id"] = findNextId()
        profesores.append(profesor)
        return profesor, 201
    else:
        return {"error":"Request must be JSON"}, 415


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5050)