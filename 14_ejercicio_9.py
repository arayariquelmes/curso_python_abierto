#Escribir un programa que reciba 2 valores enteros  y una operación string, 
#dependiendo de la operación ejecutar la suma, resta,
#multiplicación o división entre los valores

# 2 3, suma 5

n1 = int(input("Ingrese primer número:"))
n2 = int(input("Ingrese segundo número:"))
op = input("Ingrese operación:").lower()
if op == "suma":
    print(n1 + n2)
elif op == "resta":
    print(n1 - n2)
elif op == "multiplicacion":
    print(n1 * n2)
elif op == "division":
    if n2 == 0:
        print("No se puede dividir por 0")
    else:
        print(n1 / n2)
else:
    print("Operación incorrecta!")