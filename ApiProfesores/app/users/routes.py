from flask import Blueprint, request
from flask_jwt_extended import create_access_token
import bcrypt

from app.utils.leer_escribir import leeFichero, escribeFichero

#Ruta del fichero de usuarios
rutaUsuarios = "app/ficheros/users.json"

usersBP = Blueprint('users', __name__)

"""
Autentificacion de usuario
"""
@usersBP.get('/')
def login_usuario():
    if request.is_json:
        users = leeFichero(rutaUsuarios)
        user = request.get_json()
        username = user['username']
        password = user['password'].encode('utf-8')
        for userFile in users:
            if userFile['username'] == username:
                passwordFile = userFile['password']
                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token = create_access_token(identity = username)
                    return {'token':token}, 200
                else:
                    return {'error' : 'No authorized'}, 401
        return {'error' : 'User not found'}, 404
    return {"error" : "Request must be JSON"}, 415

@usersBP.post("/login")
def getUsuario():
   if request.is_json:
       user = request.get_json()
       username = user["username"]
       password = user["password"]
       usuarios = leeFichero(rutaUsuarios)
       for usuario in usuarios:
           if usuario["username"] == username and bcrypt.checkpw(password.encode("utf-8"),bytes.fromhex(usuario["password"])):
               return {"token": create_access_token(identity=username)}, 200
       return {"token":""}, 401
   return {"error": "Request must be JSON"}, 415


"""
Creacion de nuevo usuario
"""
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
        token = create_access_token(identity = new_user['username'])
        return {'token':token}, 201
    else:
        return {"error" : "JSON incorrecto"}, 415



