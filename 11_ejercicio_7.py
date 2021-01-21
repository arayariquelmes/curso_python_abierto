#Escriba un programa en Python que convierta una cantidad de dólares
#a pesos chilenos, sabiendo que el dólar esta a $840.
#El programa debe solicitar la cantidad de dólares a convertir

vd = 737
dolar = int(input("Ingrese valor en dolar:"))
peso = dolar*vd
print(f"{dolar} equivale a ${peso} chileno")
