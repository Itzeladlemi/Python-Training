"""
Project:
User Management System

Author:
Itzel Zazueta

Description:
First Python project for learning functions,
dictionaries and user management.
"""
from almacenamiento import guardar_usuarios, cargar_usuarios
from usuarios import crear_usuario, buscar_usuario, lista_usuarios, eliminar_usuario, agregar_usuario

#lista
usuarios = []

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
        agregar_usuario(usuarios)

    elif opcion == "2":
        lista_usuarios(usuarios)
    
    elif opcion == "3":
        buscar_usuario(usuarios)

    elif opcion == "4":
        eliminar_usuario(usuarios)

    elif opcion == "5":
        programa_activo = False





