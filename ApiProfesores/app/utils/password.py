import secrets
import string
import random

"""
Genera una password aleatoria de longitud aleatoria entre 8 y 12
"""
def random_password():
    #la password va a incluir caracteres ascii, digitos y simbolos de puntuacion
    characters = string.ascii_letters + string.digits + string.punctuation
    #genera un numero aleatorio entre 8 y 12 para la longitud de la contrasñea
    password_length = random.randint(8, 12)
    #genera una password aleatoria de longitud aleatoris
    random_password = ''.join(secrets.choice(characters) for _ in range(password_length))

    return random_password


