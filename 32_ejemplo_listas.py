#Ejemplo de funcionamiento de listas

personas = [] #Generar una lista vacía
print("Cantidad de personas actuales:", len(personas))
personas.append("Seba Araya") #Agregar elemento a la lista
print("Cantidad de personas actuales:", len(personas))#largo de lista

for i in range(4):
    nombre = input("Ingrese nombre de persona:")
    personas.append(nombre) #Agregar elementos dentro de un ciclo
print("Cantidad final:",len(personas))
print("Personas:",personas) #Mostrar el contenido de la lista
personas.sort()#Ordena naturalmente de menor a mayor
print("Ordenado:",personas)
personas.reverse() #Invierte la lista
print("Invertido:",personas)