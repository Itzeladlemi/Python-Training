from almacenamiento import guardar_usuarios


def crear_usuario(nombre, edad):
    return {
        "nombre": nombre,
        "edad": edad,
        "activo": True
    }


def mostrar_usuario(usuario):
    print("--- Usuario encontrado ---")
    print("Nombre:", usuario["nombre"])
    print("Edad:", usuario["edad"])
    print("Activo:", usuario["activo"])


def buscar_usuario(usuarios):
    buscar = input("Ingrese el nombre: ")

    for usuario in usuarios:
        if usuario["nombre"] == buscar:
            return usuario

    return None


def lista_usuarios(usuarios):
    if len(usuarios) == 0:
        print("No hay usuarios registrados")
    else:
        for usuario in usuarios:
            print("--USUARIO--")
            print("Nombre:", usuario["nombre"])
            print("Edad:", usuario["edad"])
            print("Activo:", usuario["activo"])


def agregar_usuario(usuarios):
    nombre = input("Ingrese su nombre: ")

    edad_valida = False

    while not edad_valida:
        edad = input("Ingrese su edad: ")

        try:
            edad = int(edad)
            edad_valida = True
        except ValueError:
            print("Edad inválida. Ingrese la edad en números.")

    usuario = crear_usuario(nombre, edad)
    usuarios.append(usuario)

    guardar_usuarios(usuarios)

    print("Usuario agregado correctamente.")


def editar_usuario(usuarios):
    usuario = buscar_usuario(usuarios)

    if usuario is None:
        print("Usuario no encontrado.")
        return

    mostrar_usuario(usuario)

    nuevo_nombre = input("Ingrese el nuevo nombre: ")

    edad_valida = False

    while not edad_valida:
        nueva_edad = input("Ingrese la nueva edad: ")

        try:
            nueva_edad = int(nueva_edad)
            edad_valida = True
        except ValueError:
            print("Edad inválida. Ingrese la edad en números.")

    usuario["nombre"] = nuevo_nombre
    usuario["edad"] = nueva_edad

    guardar_usuarios(usuarios)

    print("Usuario actualizado correctamente.")


def eliminar_usuario(usuarios):
    usuario = buscar_usuario(usuarios)

    if usuario is None:
        print("Usuario no encontrado.")
        return

    usuarios.remove(usuario)

    guardar_usuarios(usuarios)

    print("Usuario eliminado correctamente.")