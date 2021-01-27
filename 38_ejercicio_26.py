from random import randint
#Generar un programa en python que genere una
#lista de 10 números al azar entre 1 y 20.

lista = []

for i in range(10):
    lista.append(randint(1,20))

print(lista)
#[2,5,10,12,16,30,23,20]
#En base al ejercicio anterior, solicitar al usuario 10 números y
#mostrar cuantos aciertos
#tuvo al adivinar los números de la lista original.
aciertos = 0
for i in range(10):
    n = int(input("Ingrese número buscado:"))
    if lista.count(n) > 0:
        aciertos+=1
    #for j in lista:
    #    if n == j:
    #        aciertos+=1
    #        break 

print("La cantidad de aciertos es:", aciertos)
