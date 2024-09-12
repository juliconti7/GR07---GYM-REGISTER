from datetime import datetime

def validarNombre(nombre):
    if nombre.replace(" ", "").isalpha():
        return True
    else:
        return False
    
def validarDni(dni, lista):
    if dni.isdigit() and 1000000 <= int(dni) <= 99999999:
        for miembro in lista:
            if dni == miembro[1]:
                return False
        return True
    else:
        return False
    
def borrarMiembro(dni, lista):
    for i in range(len(lista)):
        if lista[i][1] == dni:
            lista.pop(i)
            print("Miembro eliminado")
            break
        else:
            print("Miembro no encontrado")
    return lista



def registrarse(lista):
    nombreCompleto = input("Ingrese su nombre y apellido: ")
    dni = input("Ingrese su DNI: ")
    fecha = datetime.now()
    if validarNombre(nombreCompleto) == True and validarDni(dni, lista) == True:
        print("Registrado con exito")
        lista.append([nombreCompleto, dni, fecha.strftime("%d-%m-%Y")])
    else:
        print("Nombre o DNI invalido")
