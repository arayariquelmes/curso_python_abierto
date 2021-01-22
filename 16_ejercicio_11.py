# Almacenes “El harapiento distinguido” tiene una promoción: 
# a todos los trajes que tienen un precio superior a $30000 
# se les aplicará un descuento de 15%, a todos los demás 
# se le aplicará sólo un 8%. Realice un programa en Python que 
# solicite el precio del traje y calcule cuanto es 
# el descuento aplicado y cuánto es lo que realmente debe cancelar.

precio = int(input("Ingrese precio del traje:"))

if precio > 30000:
    descuento = precio*0.15
else:
    descuento = precio*0.08
total = round(precio - descuento)
print("*"*20)
print(f"Precio: ${precio}")
print(f"Descuento: ${round(descuento)}")
print(f"Total a pagar: ${total}")
print("*"*20)