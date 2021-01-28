#Generar una función llamada generarRectangulo,
#que reciba base y altura de un rectángulo y
#dibuje el rectángulo usando asteriscos.
#Debe definir por defecto la base como 5 y
#la altura como 3. Solicitar los valores necesarios
#para llamar a la función
from funciones import generarRectangulo



b = int(input("Ingrese base:"))
a = int(input("Ingrese altura:"))
generarRectangulo(base=b,altura=a)