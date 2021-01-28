#Ejemplo de uso de funciones en python

def sumar(a,b):
    return a + b

def calcularIva(valor):
    return valor*0.19

lista = []
res = sumar(5,7)
iva = calcularIva(5000)

print("La suma es",res)
print("El iva de 5000 es",iva)