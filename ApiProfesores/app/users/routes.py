from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
import bcrypt

from app import users
from app.ficheros.leer_escribir import leeFichero, escribeFichero


rutaUsuarios = "app/ficheros/users.json"

usersBP = Blueprint('users', __name__)

@usersBP.get('/')
def get_usuarios():
    usuarios = leeFichero(rutaUsuarios)
    return jsonify(usuarios)

@usersBP.post('/')
def add_usuario():
    lista = leeFichero(rutaUsuarios)

    if request.is_json:
        #recibe un diccionario con username y password
        new_user = request.get_json()
        #pillo la contraseña del usuario
        contra = new_user ["password"].encode('utf-8')
        #esa es la contraseña que hay que cifrar con hash
        sal = bcrypt.gensalt()

        hashPassword = bcrypt.hashpw(contra, sal).hex()
        new_user['password'] = hashPassword
        lista.append(new_user)
        escribeFichero(rutaUsuarios, lista)
        token = create_access_token(identity = new_user["username"])
        return {'token':token}, 201
    else:
        return {"error" : "JSON incorrecto"}, 415

