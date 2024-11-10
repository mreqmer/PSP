from time import sleep

from pip._vendor import requests

apiUrl = "http://localhost:5000/users/login"


def login_usuarios():
    username = input("User: ")
    password = input("Password: ")
    print(username, password)
    resultado = requests.post(apiUrl, json={"username": username, "password": password}, headers={"Content-Type": "application/json"})
    token = resultado.json().get("token")
    return token

def usar_token(token):
    try:
        response = requests.get(apiUrl, headers={"Authorization": "Bearer " + token})
    except Exception as e:
        print(e)
    # Si la petición es exitosa
    if response.status_code == 200:
        # Muestra el json correspondiente a la petición
        print(response.json())
    # Si no, muestra este mensaje
    else:
        print("Se ha producido un error" + str(response.status_code))
    sleep(2)  # Pausa la ejecución durante 2 segundos

