from flask import Flask
from flask_jwt_extended import JWTManager
from .utils.password import *
from .profesores.routes import profesoresBP
from .asignaturas.routes import asignaturasBP
from .users.routes import usersBP

app = Flask(__name__)
app.register_blueprint(profesoresBP, url_prefix='/profesores')
app.register_blueprint(asignaturasBP, url_prefix='/asignaturas')
app.register_blueprint(usersBP, url_prefix='/users')

#Secret_Key siempre se pone, el token_generado es el token que se usa para acceder
app.config['JWT_SECRET_KEY'] = random_password()

jwt = JWTManager(app)