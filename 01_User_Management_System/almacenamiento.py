import json

def guardar_usuarios(usuarios):
    with open("01_User_Management_System/datos.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

def cargar_usuarios():
    try:
        with open("01_User_Management_System/datos.json", "r") as archivo:
            return json.load(archivo)
    except:
        return []