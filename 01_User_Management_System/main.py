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
    
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

usuario = crear_usuario(nombre, int(edad))

usuarios.append(usuario)

respuesta = input("¿Desea agregar otro usuario? (s/n): ")
while respuesta == "s":
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    usuario = crear_usuario(nombre, int(edad))
    usuarios.append(usuario)
    respuesta = input("¿Desea agregar otro usuario? (s/n): ")
    
for usuario in usuarios:
    print("--USUARIO--")
    print("Nombre:", usuario["nombre"])
    print("Edad:", usuario["edad"])
    print("Activo:", usuario["activo"])