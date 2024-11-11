from app.zenderismo.routes import rutasBP
from app.users.routes import usersBP
from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
#bp para las rutas de zenderismo
app.register_blueprint(rutasBP, url_prefix='/rutas')
#bp para los usuarios registrados en zenderismo
app.register_blueprint(usersBP, url_prefix='/users')

#Secret_Key para cifrar las contraseñas de los usuarios
app.config['JWT_SECRET_KEY'] = "password"

jwt = JWTManager(app)