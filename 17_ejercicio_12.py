#Escriba un programa en Python que solicite un numero por teclado y 
#muestre si el numero es par (múltiplo de 2) o impar

numero = int(input("Ingrese número:"))
if numero % 2 == 0:
    print("El número",numero, "es par")
else:
    print("El número",numero,"es impar")