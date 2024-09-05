from datetime import datetime
def borrarMiembro(nombre):
    for i in range(len(inscriptos)):
        if inscriptos[i][0] == nombre:
            inscriptos.pop(i)
            print("Miembro eliminado")
            break
        else:
            print("Miembro no encontrado")
    return inscriptos


inscriptos = []


print(".1 Mostras inscriptos")
print(".2 Inscribirme")
print(".3 Borrar miembro")
print(".4 Salir")

opcion= int(input("introduce una opcion: "))

while opcion != 4:
      

    if opcion == 1:
        print(inscriptos)
    elif opcion == 2:
        nombre = input("Insgrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        ahora = datetime.now()
        fecha_formateada = ahora.strftime("%d-%m-%Y")
        inscriptos.append([nombre, apellido, fecha_formateada])
        print(inscriptos)
    elif opcion == 3:
        nombreBorrar = input("Ingrese el nombre del miembro a borrar: ")
        borrarMiembro(nombreBorrar)

        
    else: 
        print("Saliendo") 
        opcion =3
    opcion= int(input("introduce una opcion: "))