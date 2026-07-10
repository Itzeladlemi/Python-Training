"""
Project:
User Management System

Author:
Itzel Zazueta

Description:
First Python project for learning functions,
dictionaries and user management.
"""

from almacenamiento import cargar_usuarios
from usuarios import (
    agregar_usuario,
    buscar_usuario,
    mostrar_usuario,
    lista_usuarios,
    eliminar_usuario,
    editar_usuario,
)

# Lista de usuarios
usuarios = cargar_usuarios()

programa_activo = True

while programa_activo:
    print("\n--- MENÚ ---")
    print("1. Agregar usuario")
    print("2. Mostrar usuarios")
    print("3. Editar usuario")
    print("4. Buscar usuario")
    print("5. Eliminar usuario")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_usuario(usuarios)

    elif opcion == "2":
        lista_usuarios(usuarios)

    elif opcion == "3":
        editar_usuario(usuarios)

    elif opcion == "4":
        usuario = buscar_usuario(usuarios)

        if usuario is None:
            print("Usuario no encontrado.")
        else:
            mostrar_usuario(usuario)

    elif opcion == "5":
        eliminar_usuario(usuarios)

    elif opcion == "6":
        programa_activo = False
        print("Programa finalizado.")

    else:
        print("Opción inválida. Intente nuevamente.")