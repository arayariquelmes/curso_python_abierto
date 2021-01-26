#Escribir un programa que solicite 3 números distintos por teclado, 
#y calcule el número mayor ingresado..

#Forma cualquier lenguaje de programación
n1 = int(input("Ingrese número 1:"))
n2 = int(input("Ingrese número 2:"))
n3 = int(input("Ingrese número 3:"))

mayor = n1
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3
print("El mayor es:",mayor)

#Forma Python
print("El mayor es:", max(n1,n2,n3))
print("El menor es:", min(n1,n2,n3))

