#import os
#Ejemplos de uso del ciclo while

#1. Ciclo que se repite una cantidad indeterminada de veces

res="si"
while res == "si":
    print("Bienvenido al programa!")
    res = input("Desea continuar?")
    #Esto limpia la pantalla
    #os.system('clear')
print("Gracias por utilizar el super programa más util del mundo")


#2. Ciclo que se repite un número finito de veces
cont = 1
while cont <= 100:
    print(cont, end=" ")
    cont+=1 # cont = cont + 1
print("Se acabó!!")