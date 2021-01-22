# Genere un archivo llamado repetir.py que solicite 
# al usuario una palabra y una cantidad. 
# Posteriormente debe mostrar por pantalla la palabra
# repetida la cantidad de veces escrita.

palabra = input("Digame una palabra:")
cantidad = 0
while cantidad <=0:
    cantidad = int(input("Ingrese cantidad:"))

cont = 1
while cont <= cantidad:
    print(palabra)
    cont+=1

#Forma python:
print("Forma Python:")
print((palabra+"\n")*cantidad)