#Escribir una función que reciba una
#muestra de números en una lista y devuelva otra
#lista con sus cuadrados. Solicitar 5 números,
#almacenarlos en una lista y mostrar el
#resultado de la llamada a la función

def cuadrados(lista):
    lista_cuadrados = []
    for n in lista:
        lista_cuadrados.append(n**2)
    return lista_cuadrados

numeros = []
for i in range(5):
    n=None
    while n is None:
        try:
            n = int(input("Ingrese numero"))
        #except ValueError as e:
        except:
            n = None
            print("Debe ingresar un valor numérico")
        # except ZeroDivisionError as e:
        #     print("Division por 0")
        # except Exception as e:
        #     print("Error general")
    numeros.append(n)

print("Originales",numeros)
print("Al cuadrado", cuadrados(numeros))