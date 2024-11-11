from flask import Blueprint, request
from flask_jwt_extended import create_access_token
import bcrypt

from app.recursos.leer_escribir import leeFichero, escribeFichero

usersBP = Blueprint('users', __name__)
#fichero con los usuarios
rutaUsuarios = "app/ficheros/users.json"


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

"""
Hace el login de usuario
"""
@usersBP.post("/login")
def getUsuario():
   if request.is_json:
       user = request.get_json()
       username = user["username"]
       password = user["password"]
       usuarios = leeFichero(rutaUsuarios)
       #busca al usuario que intenta logear para comporbar las credenciales y compara la password con su cifrada
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
        #se cifra la password
        hashPassword = bcrypt.hashpw(contra, sal).hex()
        new_user['password'] = hashPassword
        #se añade el nuevo usuario
        lista.append(new_user)
        #escribe en el fichero
        escribeFichero(rutaUsuarios, lista)
        #se genera un token y se devuelve
        token = create_access_token(identity = new_user['username'])
        return {'token':token}, 201
    else:
        #error
        return {"error" : "JSON incorrecto"}, 415

