from almacenamiento import guardar_usuarios

def buscar_usuario(usuarios):
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

def lista_usuarios(usuarios):
        if len(usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            for usuario in usuarios:
                print("--USUARIO--")
                print("Nombre:", usuario["nombre"])
                print("Edad:", usuario["edad"])
                print("Activo:", usuario["activo"])

def eliminar_usuario(usuarios):
    eliminar = input("Ingrese el nombre del usuario a eliminar: ")
    encontrado = False

    for usuario in usuarios:
        if usuario["nombre"] == eliminar:
                encontrado = True
                usuarios.remove(usuario)
                guardar_usuarios(usuarios)
                print("Usuario eliminado correctamente.")
                break
    
    if not encontrado:
             print("Usuario no encontrado.")

def agregar_usuario(usuarios):
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
    guardar_usuarios(usuarios)

def crear_usuario(nombre, edad):
    return {
        "nombre": nombre,
        "edad": edad,
        "activo": True
    }