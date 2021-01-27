#Escribir un programa que almacena en una lista los números
#pares desde 1 hasta N donde N es entregado por el usuario. 
#Posteriormente mostrarla por pantalla elemento a elemento

n = int(input("Ingrese número final"))

pares=[]
#Esto hace lo mismo que el for
#i = 1
#while i < n:
#    if i % 2 == 0:
#        pares.append(i)
#    i+=1
#Esto hace lo mismo que la compresion
#for i in range(1,n+1):
#    if i % 2 ==0:
#        pares.append(i)

#Compresión de lista:
pares = [i for i in range(1,n+1) if i % 2 ==0]
print(pares)