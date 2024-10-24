from flask import Flask
from flask_jwt_extended import JWTManager
from .profesores.routes import profesoresBP
from .asignaturas.routes import asignaturasBP
from .users.routes import usersBP

app = Flask(__name__)
app.register_blueprint(profesoresBP, url_prefix='/profesores')
app.register_blueprint(asignaturasBP, url_prefix='/asignaturas')
app.register_blueprint(usersBP, url_prefix='/users')

#Secret_Key siempre se pone, el token_generado es el token que se usa para acceder
app.config['Secret_Key'] = 'token_generado'

jwt = JWTManager(app)