#Escribe un programa python que pida un número por teclado
#y que cree un diccionario cuyas claves sean desde el
#número 1 hasta el número indicado, y
#los valores sean los cuadrados de las claves.


n = int(input("Ingrese numero:"))

numeros = {}

for i in range(1, n + 1):
    numeros[i] = i**2

print(numeros)

print("Las claves",numeros.keys())
print("Los valores", numeros.values())

for clave,valor in numeros.items():
    print("Clave:",clave,"Valor:",valor)


#Codifica un programa en python que nos permita guardar
#los nombres de los alumnos de una clase y las notas que han obtenido.
#Cada alumno puede tener distinta cantidad de notas.
#Guarda la información en un diccionario cuya claves
#serán los nombres de los alumnos y los valores serán
#listas con las notas de cada alumno.