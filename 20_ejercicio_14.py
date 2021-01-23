#Escriba un programa que pida al usuario
#ingresar un numero y éste muestre la tabla de
#multiplicar del numero ingresado.

n = int(input("Ingrese el número:"))

i = 1
while i <= 10:
    print(f"{n} * {i} = {n*i}")
    i+=1
