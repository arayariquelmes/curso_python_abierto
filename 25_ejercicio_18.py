#Escribir un programa que
#pida al usuario una palabra y luego
#muestre por pantalla una a una las letras
#de la palabra introducida.

palabra = input("Digame una palabra:")
print("Palabra al derecho")
for letra in palabra:
    print(letra, end = " ")
print()
print("Palabra al revez")
for letra in reversed(palabra):
    print(letra, end = " ")
print()
print("Ordenada alfabeticamente")
for letra in sorted(palabra):
    print(letra, end=" ")
