#Escribir un programa que
#pida al usuario un número entero positivo y
#muestre por pantalla la cuenta atrás desde ese
#número hasta cero separados por comas.

n = -1

while n <=0:
    n = int(input("Ingresar número positivo"))

cont = n

while cont >=0:
    final = ','
    if cont == 0:
        final = '\n'
    print(cont, end=final)
    cont-=1 #cont = cont - 1

