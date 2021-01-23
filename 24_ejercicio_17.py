#Escribir un programa en Python
#que solicite un numero y calcule la
#suma de 1+2+3….numero.

n = int(input("Ingrese un numero"))
suma = 0
for i in range(1, n + 1):
    suma+=i #suma = suma + i

print("La suma es:",suma)