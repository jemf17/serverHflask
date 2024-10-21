from dotenv import load_dotenv
import os
import requests

load_dotenv()

def save_img(img, ruta):
    api_img = os.getenv('API_IMAGE') +'/'+ ruta
    response = requests.post(api_img, files=img)
    if response.status_code != 200:
        return -1
    return create_url(api_img, response.json()['message'])

def create_url(ruta, name):
    return ruta +'/'+ name
