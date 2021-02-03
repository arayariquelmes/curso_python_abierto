#Generar un script agenda.py que permita
#solicitar nombre, apellido y teléfono de
#personas hasta que el usuario no desee continuar.
#Por cada contacto se guarden en un archivo llamado agenda.txt
#en formato csv (separador ;)

def guardarEnArchivo(contacto):
    archivo = open("agenda.txt", "a")
    linea = contacto["nombre"] + ";" + contacto["apellido"] +";" + contacto["telefono"] + "\n"
    archivo.write(linea)
    archivo.close()
res = "si"

while res == "si":

    nombre = input("Ingrese nombre")
    apellido = input("Ingrese apellido")
    telefono = input("Ingrese telefono")

    contacto = {'nombre':nombre, 'apellido':apellido, 'telefono':telefono}
    guardarEnArchivo(contacto)
    res = input("Desea continuar?si/no:").lower()




