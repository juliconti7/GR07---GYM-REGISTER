from datetime import datetime
from funciones import borrarMiembro, registrarse

def main():
    usuarios = []
    print("Bienvenido al sistema de registro de miembros")
    print(".1 Registrarse")
    print(".2 Lista de miembros")
    print(".3 Borrar miembro")
    print(".0 Salir")

    opcion= int(input("introduce una opcion: "))
    while opcion != 0:
        if opcion == 1:
            registrarse(usuarios)
        elif opcion == 2:
            print("Nombres\t\tDNI\t\tFecha")
            for i in usuarios:
                print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}")
        elif opcion == 3:
            dniBorrar = input("Ingrese el DNI del miembro a borrar: ")
            borrarMiembro(dniBorrar, usuarios)
        
        opcion= int(input("introduce una opcion: "))
    print("Hasta luego")



main()