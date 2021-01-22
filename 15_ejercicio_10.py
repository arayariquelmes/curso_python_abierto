#Crear un archivo conversor.py que contenga un programa que
#convierta de centímetros a pulgadas. 
#Una pulgada es igual a 2.54 centímetros.
cm = float(input("Ingrese valor en centimetros"))
pulgadas = cm/2.54
print(f"el valor {cm} es igual a {round(pulgadas,2)}\"")