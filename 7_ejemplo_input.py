print("Ingrese su rut:")
rut = input()
print("Ingrese su nombre:")
nombre = input()
print("Ingrese su apellido:")
apellido = input()
print("Ingrese su edad:")
edad = int(input())

print("*"*20)
print(" "*3,"DATOS PERSONALES", " "*3)
print("*"*20)
print()
print("NOMBRE:",nombre.upper(),apellido.upper())
print("RUT:",rut)
print("EDAD:",edad)
print("*"*20)
edad10 = edad + 10
print("Su edad dentro de 10 años será",edad10)
#soliciten: apellido, edad, rut