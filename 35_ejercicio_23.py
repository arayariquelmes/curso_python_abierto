#Escribir un programa que almacene un conjunto de notas,
#y determine el promedio de todas las notas
#y la posición de la nota más alta.

res = "si"
notas = []

while res == "si":
    nota = float(input("Ingrese nota:"))
    notas.append(nota)
    res = input("Desea continuar?").strip().lower()

prom = round(sum(notas)/len(notas),1)
print("El promedio de las notas es:",prom)
alta = notas.index(max(notas)) #5.5,6,7,2
print("El indice de la nota más alta es",alta)