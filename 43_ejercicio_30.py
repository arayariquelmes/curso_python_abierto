#Llamar a la función descrita en el ejercicio
#anterior para generar 10 rectángulos con
#largo y alto al azar
#Para agregar funciones a la path
#import sys
#sys.path.append("/home/me/mypy") 
from funciones import generarRectangulo
from random import randint

for i in range(10):
    base = randint(4,15)
    alto = randint(4,15)
    generarRectangulo(base,alto)

