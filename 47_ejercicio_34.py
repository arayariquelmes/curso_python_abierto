#Codifica un programa en python que nos permita guardar
#los nombres de los alumnos de una clase y las notas que han
#obtenido. Cada alumno puede tener distinta cantidad de notas.
#Guarda la información en un diccionario cuya claves serán
#los nombres de los alumnos y
#los valores serán listas con las notas de cada alumno.
def solicitarNotas():
    notas= []
    res = "si"
    while res =="si":
        n = float(input("Ingrese nota del estudiante:"))
        notas.append(n)
        res = input("Desea continuar?si/no:").lower()
    return notas
curso = []

res = "si"
while res == "si":
    nombre = input("Ingrese nombre")
    estudiante = {}
    estudiante['nombre'] = nombre
    estudiante['notas'] = solicitarNotas()
    curso.append(estudiante)
    res = input("Desea continuar? si/no").lower()
print(curso)