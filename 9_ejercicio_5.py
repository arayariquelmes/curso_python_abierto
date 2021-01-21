#Escriba un programa en Python que calcule el área y 
#el perímetro de un rectángulo.
#El programa de solicitar la base y la altura para calcular lo solicitado.

base = int(input("Ingrese base:"))
altura = int(input("Ingrese altura:"))

perimetro = 2*base + 2*altura
area = base*altura

print(f"El area es {area}")
print(f"El perimetro es {perimetro}")
