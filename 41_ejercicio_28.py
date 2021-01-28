#Realiza una función llamada area_circulo(radio)
#que devuelva el área de un círculo a
#partir de un radio. Calcula el área de un
#círculo de 5 de radio.
#El área de un círculo se obtiene al elevar
#el radio a dos y multiplicando el resultado
#por el número pi
from math import pi

def area_circulo(radio):
    return pi*radio**2

area = area_circulo(5)
print(round(area,2))