#Escribir un programa que 
#calcule el IMC (indice de masa corporal) 
#e indique cuál es el estado según 
#la siguiente tabla.

peso = float(input("Ingrese peso:"))
estatura = float(input("Ingrese estatura:"))

imc = peso/(estatura**2)

if imc < 19:
    print("Bajo peso")
elif imc >=19 and imc < 25:
    print("Normal")
elif imc >=25 and imc <=30:
    print("Sobrepeso")
else:
    print("Obesidad")
