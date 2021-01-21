#Escriba un programa en Python que calcule el promedio de tres notas
#El programa de solicitar cada nota y entregar el resultado

n1 = float(input("Ingrese primera nota:"))
n2 = float(input("Ingrese segunda nota:"))
n3 = float(input("Ingrese tercera nota:"))

prom = (n1 + n2 + n3)/3
print("El promedio es:",round(prom,2))