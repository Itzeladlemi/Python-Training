"""
Project:
User Management System

Author:
Itzel Zazueta

Description:
First Python project for learning functions,
dictionaries and user management.
"""
import json

#lista
usuarios = []

#Función
def crear_usuario(nombre, edad):
    usuario = {
        "nombre": nombre,
        "edad": edad,
        "activo": True
    }
    return usuario

#Función para json
def guardar_usuarios():
    with open("01_User_Management_System/datos.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

def cargar_usuarios():
    try:
        with open("01_User_Management_System/datos.json", "r") as archivo:
            return json.load(archivo)
    except:
        return []

usuarios = cargar_usuarios()
    
programa_activo = True
while programa_activo:
    print("--Menu--")
    print("1. Agregar usuario")
    print("2. Mostrar usuarios")
    print("3. Buscar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")
    opcion = input("Seleccione opcion: ")
    
    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
        edad_valida = False
        while not edad_valida:
            edad = input("Ingrese su edad: ")
            try:
                edad = int(edad)
                edad_valida = True
            except:
                print("Edad inválida. Ingrese la edad en números.")

        usuario = crear_usuario(nombre, edad)
        usuarios.append(usuario)
        guardar_usuarios()
    
    elif opcion == "2":
        if len(usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            for usuario in usuarios:
                print("--USUARIO--")
                print("Nombre:", usuario["nombre"])
                print("Edad:", usuario["edad"])
                print("Activo:", usuario["activo"])
    
    elif opcion == "3":
        buscar = input("Ingrese el nombre: ")
        encontrado = False

        for usuario in usuarios:
            if usuario["nombre"] == buscar:
                print("--- Usuario encontrado ---")
                print("Nombre:", usuario["nombre"])
                print("Edad:", usuario["edad"])
                print("Activo:", usuario["activo"])
                encontrado = True
                break

        if not encontrado:
            print("Usuario no encontrado.")

    elif opcion == "4":
        eliminar = input("Ingrese el nombre del usuario a eliminar: ")
        encontrado = False
        for usuario in usuarios:
            if usuario["nombre"] == eliminar:
                encontrado = True
                usuarios.remove(usuario)
                guardar_usuarios()
                print("Usuario eliminado correctamente.")
                break
        if not encontrado:
             print("Usuario no encontrado.")

    elif opcion == "5":
        programa_activo = False