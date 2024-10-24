#
# from flask import *
#
#
# app = Flask(__name__)
#
# profesores = [
#     {"id": 1, "nombre":"Juan", "apellidos":"Barrena","telefono":"666555444", "direccion":"C/calle bonita", "cc":"ES1234"},
#     {"id": 2, "nombre":"Maria", "apellidos":"Buenavilla","telefono":"666555444", "direccion":"C/calle bonita", "cc":"ES4321"},
#     {"id": 3, "nombre":"Pedro", "apellidos":"Mapache","telefono":"666555444", "direccion":"C/calle bonita", "cc":"ES5555"},
# ]
#
# asignaturas = [
#     {"id": 1, "titulo":"Programacion", "numHoras": "60", "idProfesor":"1"},
#     {"id": 2, "titulo":"Empresa", "numHoras": "20", "idProfesor":"2"},
#     {"id": 3, "titulo":"Base de datos", "numHoras": "45", "idProfesor":"1"},
#     {"id": 4, "titulo":"Html", "numHoras": "50", "idProfesor":"3"},
#     {"id": 5, "titulo":"Sistemas", "numHoras": "30", "idProfesor":"3"},
#
# ]
#
# @app.route('/')
# def index():
#     return 'Hola a todos!'
#
# """
# Métodos get para los profesores
# """
# #Get profesor
# @app.get("/profesores")
#
# def get_profesores():
#     return jsonify(profesores)
# #Get para un unico profesor
# @app.get("/profesores/<int:id>")
# def get_profesor(id):
#     for profesor in profesores:
#         if profesor["id"] == id:
#             return profesor, 200
#     return {"error":"Profesor not found"}, 404
#  #Post, sube un profesor nuevo
# @app.post("/profesores")
# def add_profesor():
#     if request.is_json:
#         profesor = request.get_json()
#         profesor["id"] = findNextIdProfesor()
#         profesores.append(profesor)
#         return profesor, 201
#     else:
#         return {"error":"Request must be JSON"}, 415
# #actualiza un profesor entero
# @app.put("/profesores/<int:id>")
# @app.patch("/profesores/<int:id>")
# def update_profesor(id):
#     if request.is_json:
#         newProfesor = request.get_json()
#         for profesor in profesores:
#             if profesor["id"] == id:
#                 for element in newProfesor:
#                     profesor[element] = newProfesor[element]
#
#                 return profesor, 200
#     return {"error":"Request must be JSON"}, 415
#
# #borra a un profesor
# @app.delete("/profesores/<int:id>")
# def delete_profesor(id):
#     for profesor in profesores:
#         if profesor["id"] == id:
#             profesores.remove(profesor)
#             return {}, 200
#
#     return {"error":"Profesor not found"}, 404
#
# """
# Métodos get para las asignaturas
# """
# #Get Asignatura
# @app.get("/asignaturas")
#
# def get_asignaturas():
#     return jsonify(asignaturas)
# #Get para un unico profesor
# @app.get("/asignaturas/<int:id>")
# def get_asignatura(id):
#     for asignatura in asignaturas:
#         if asignatura["id"] == id:
#             return asignatura, 200
#     return {"error":"Asignatura not found"}, 404
#
# @app.get("/asignaturas/<int:id>")
# def get_asignatura(id):
#     for asignatura in asignaturas:
#         if asignatura["id"] == id:
#             return asignatura, 200
#     return {"error":"Asignatura not found"}, 404
#
#  #Post, sube una asignatura nueva
# @app.post("/asignaturas")
# def add_asignatura():
#     if request.is_json:
#         asignatura = request.get_json()
#         asignatura["id"] = findNextIdAsignatura()
#         asignaturas.append(asignatura)
#         return asignatura, 201
#     else:
#         return {"error":"Request must be JSON"}, 415
#
# #actualiza una asignatura entera
# @app.put("/asignaturas/<int:id>")
# @app.patch("/asignaturas/<int:id>")
# def update_asignatura(id):
#     if request.is_json:
#         newAsignatura = request.get_json()
#         for asignatura in asignaturas:
#             if asignatura["id"] == id:
#                 for element in newAsignatura:
#                     asignatura[element] = newAsignatura[element]
#
#                 return asignatura, 200
#     return {"error":"Request must be JSON"}, 415
#
# #borra a una asignatura
# @app.delete("/asignaturas/<int:id>")
# def delete_asignatura(id):
#     for asignatura in asignaturas:
#         if asignatura["id"] == id:
#             asignaturas.remove(asignatura)
#             return {}, 200
#
#     return {"error":"Asignatura not found"}, 404
#
#
# """
# Busca el siguiente id de un profesor
# """
# def findNextIdProfesor():
#     return max(profesor["id"] for profesor in profesores) + 1
#
# """
# Busca el siguiente id de una asignatura
# """
# def findNextIdAsignatura():
#     return max(asignatura["id"] for asignatura in asignaturas) + 1
#
#
#
#
# if __name__ == '__main__':
#
#     app.run(debug=True, host='0.0.0.0', port=5050)