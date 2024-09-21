from datetime import datetime
import json

def registrarUsuario():
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingresa el apellido: ")
    dni = int(input("Ingresa el DNI: "))
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    validarDni = lambda dni: len(str(dni)) == 8
    if validarDni(dni):
        # ABRIMOS EL ARCHIVO JSON
        try:
            with open('usuarios.json', 'r') as archivo:
                usuarioDiccionario = json.load(archivo)
        except FileNotFoundError:
            usuarioDiccionario = []

        # si el dni ya esta en nuestra lista de usuarios, no lo registramos
        for usuario in usuarioDiccionario:
            if usuario["dni"] == dni:
                print("El DNI ya está registrado.")
                return

        # Creamos diccionario usuario
        usuario = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "fecha_registro": fecha_actual
        }

        # lo metemos al json
        usuarioDiccionario.append(usuario)

        # Guardar los datos 
        with open('usuarios.json', 'w') as archivo:
            json.dump(usuarioDiccionario, archivo, indent=4)

        print("Usuario registrado con éxito.")
    else: 
        print("DNI inválido, debe tener 8 dígitos.")

def borrarMiembro():
    dni = int(input("Ingresa el DNI del miembro a borrar: "))

    # ABRIMOS EL ARCHIVO JSON igual que antes
    try:
        with open('usuarios.json', 'r') as archivo:
            usuarioDiccionario = json.load(archivo)
    except FileNotFoundError:
        usuarioDiccionario = []

    # Buscamos el usuario por su dni y si lo encontramos lo borramos
    for usuario in usuarioDiccionario:
        if usuario["dni"] == dni:
            usuarioDiccionario.remove(usuario)
            print("Usuario eliminado con éxito.")
            break
    else:
        print("Usuario no encontrado.")

    # Guardar los datos 
    with open('usuarios.json', 'w') as archivo:
        json.dump(usuarioDiccionario, archivo, indent=4)

def listarMiembros():
    # ABRIMOS EL ARCHIVO JSON
    try:
        with open('usuarios.json', 'r') as archivo:
            usuarioDiccionario = json.load(archivo)
    except FileNotFoundError:
        usuarioDiccionario = []

    # Mostramos los usuarios
    for usuario in usuarioDiccionario:
        print("Nombre: ", usuario["nombre"])
        print("Apellido: ", usuario["apellido"])
        print("DNI: ", usuario["dni"])
        print("Fecha de registro: ", usuario["fecha_registro"])
        print("")

def buscarMiembro():
    dni = int(input("Ingresa el DNI del miembro a buscar: "))

    # ABRIMOS EL ARCHIVO JSON igual que antes
    try:
        with open('usuarios.json', 'r') as archivo:
            usuarioDiccionario = json.load(archivo)
    except FileNotFoundError:
        usuarioDiccionario = []

    # Buscamos el usuario por su dni igual que antes, si lo encontramos lo mostramos
    for usuario in usuarioDiccionario:
        if usuario["dni"] == dni:
            print("Nombre: ", usuario["nombre"])
            print("Apellido: ", usuario["apellido"])
            print("DNI: ", usuario["dni"])
            print("Fecha de registro: ", usuario["fecha_registro"])
            break
    else:
        print("Usuario no encontrado.")

    # Guardar los datos 
    with open('usuarios.json', 'w') as archivo:
        json.dump(usuarioDiccionario, archivo, indent=4)

def main():
    print("Bienvenido al sistema de registro de miembros")
    print(".1 Registrarse")
    print(".2 Lista de miembros")
    print(".3 Borrar miembro")
    print(".4 Buscar miembro")
    print(".0 Salir")
    
    opcion= int(input("introduce una opcion: "))
    while opcion != 0:
        if opcion == 1:
            registrarUsuario()
        elif opcion == 2:
            listarMiembros()
        elif opcion == 3:
            borrarMiembro()
        elif opcion == 4:
            buscarMiembro()
        
        opcion= int(input("introduce una opcion: "))
    print("Hasta luego")


main()