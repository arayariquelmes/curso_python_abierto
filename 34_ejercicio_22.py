#Escribir un programa que almacene en una
#lista los números del 1 al 10 y los muestre por
#pantalla en orden inverso separados por comas.

lista = [x for x in range(1,11)]

#Esto es lo mismo de arriba
#lista = []
#for x in range(1,11):
#    lista.append(x)

#lista.reverse()

for n in reversed(lista):
    final = ","
    if n == lista[0]:
        final = "\n"
    print(n,end=final)
