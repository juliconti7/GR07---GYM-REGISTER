from datetime import datetime
import json

def registrarUsuario():
    nombre_valido = False
    apellido_valido = False
    dni_valido = False

    # Pedimos el nombre y lo validamos
    nombre = input("Ingresa el nombre: ")
    validarTexto = lambda nombre: nombre.isalpha()
    while nombre_valido == False:
        if validarTexto(nombre) == False:
            print("Nombre inválido, debe contener solo letras.")
            nombre = input("Ingresa el nombre: ")
        else:
            nombre_valido = True
    # Pedimos el apellido y lo validamos        
    apellido = input("Ingresa el apellido: ")
    while apellido_valido == False:
        if validarTexto(apellido) == False:
            print("Apellido inválido, debe contener solo letras.")
            apellido = input("Ingresa el apellido: ")
        else:
            apellido_valido = True
    # Pedimos el dni y lo validamos        
    dni = input("Ingresa el DNI: ")
    while dni_valido == False:
        if not dni.isdigit() and len(dni) != 8:
            print("DNI inválido, debe contener solo números y tener 8 dígitos.")
            dni = input("Ingresa el DNI: ")
        if not dni.isdigit():
            print("DNI inválido, debe contener solo números")
            dni = input("Ingresa el DNI: ")
        if len(dni) != 8:
            print("DNI inválido, debe tener 8 dígitos.")
            dni = input("Ingresa el DNI: ")
        
        else:
            dni_valido = True
    dni = int(dni)
        
    fecha_actual = datetime.now().strftime("%d-%m-%Y")

    if dni_valido == True:
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

def borrarMiembro():
    dni = int(input("Ingresa el DNI del miembro a borrar: "))
    validarDni = lambda dni: len(str(dni)) == 8
    if validarDni(dni):
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
    else:
        print("DNI inválido, debe tener 8 dígitos.")

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
    validarDni = lambda dni: len(str(dni)) == 8
    validarDni(dni)
    if validarDni(dni):
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
    else:
        print("DNI inválido, debe tener 8 dígitos.")

def main():
    print("\nBienvenido al sistema de registro de miembros")
    opcion = -1 
    while opcion != 0:
        print("\nElige una opción")
        print("1. Registrarse")
        print("2. Lista de miembros")
        print("3. Borrar miembro")
        print("4. Buscar miembro")
        print("0. Salir")

        opcion = input("Introduce una opción: ")
        
        if not opcion.isdigit():
            print("Por favor, introduce un valor numérico.")
            continue
        
        opcion = int(opcion)
        
        if opcion == 1:
            registrarUsuario()
        elif opcion == 2:
            listarMiembros()
        elif opcion == 3:
            borrarMiembro()
        elif opcion == 4:
            buscarMiembro()
        elif opcion == 0:
            print("Hasta luego")
        else:
            print("Selecciona una opción correcta")

main()