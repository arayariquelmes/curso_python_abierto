#Ejemplo de la estructura de control if

#numero = int(input("Ingrese numero:"))
#1. if solitario
#if numero < 100:
#    print("El numero era menor que 100!!")
#    print("Esta linea se ejecuta igual dentro del if")
#print("Esto se va a mostrar igual sea el numero < 100  o no")

#2. if con condicion verdadera y falsa
#promedio = float(input("Ingrese el promedio de notas:"))

# if promedio >=3.95:
#     print("Aprobado!")
#     print("Puede hacer el siguiente curso!")
# else:
#     print("Reprobado!")
#     print("Debe repetir el curso")
# print("Gracias por usar nuestra aplicación")

#3. if con multiples condiciones

promedio = float(input("Ingrese el promedio de notas:"))

if promedio >= 3.95:
    print("Aprobado!")
    print("Felicidades!!")
elif promedio >=3.0:
    print("Debe rendir examen de repetición")
    print("Contacte al Docente")
else:
    print("Reprobado!")
    print("Debe tomar proximo semestre")
print("Gracias por usar nuestra aplicación")