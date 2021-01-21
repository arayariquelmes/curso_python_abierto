#Escriba un programa en Python que calcule el índice de masa
#corporal IMC basado en la siguiente formula.
#IMC = peso/altura^2
#El programa de solicitar el peso y la altura para calcular el IMC.

peso= int(input("Ingrese peso:"))
altura = float(input("Ingrese estatura:"))
imc = peso/altura**2
print(f"Su imc es: {round(imc,1)}")

