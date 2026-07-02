"""
Project:
User Management System

Author:
Itzel Zazueta

Description:
First Python project for learning functions,
dictionaries and user management.
"""

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
    
programa_activo = True
while programa_activo:
    print("--Menu--")
    print("1. Agregar usuario")
    print("2. Mostrar usuarios")
    print("3. Salir")
    opcion = input("Seleccione opcion: ")
    
    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
        edad = input("Ingrese su edad: ")
        usuario = crear_usuario(nombre, int(edad))
        usuarios.append(usuario)
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
        programa_activo = False