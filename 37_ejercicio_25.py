#Generar una lista con las letras del abecedario,
#posteriormente generar otra lista con solo las letras 
#que se encuentran en posiciones
#pares de la lista original.

#Esto es lo mismo que con la compresión
#abecedario = []
#for i in range(ord('a'), ord('z')+1):
#    abecedario.append(chr(i))

abecedario = [chr(i) for i in range(ord('a'), ord('z')+1)]
print("El abecedario!:")
print(abecedario)
#Esto tambien hace lo mismo que abajo
#abecePar = []
#for i in range(len(abecedario)):
#    if i % 2 == 0:
#        abecePar.append(abecedario[i])
abecePar = [abecedario[i] for i in range(len(abecedario)) if i % 2 == 0]
print("Solo posiciones pares!:")
print(abecePar)