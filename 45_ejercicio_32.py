#Generar una función que llamada
#escribirTablaMultiplicar, que reciba un valor y un límite,
#que muestre por pantalla la tabla de multiplicar del
#valor desde 1 hasta el limite. El limite debe ser por
#defecto 10. Solicitar los datos requeridos para ejecutar la función

def escribirTablaMultiplicar(valor,limite=10):

    for i in range(1,limite+1):
        print(valor,"*",i,"=",valor*i)


v = None
while v is None:
    try:
        v = int(input("Ingrese valor:"))
    except:
        v = None
        print("Debe ingresar un número")

escribirTablaMultiplicar(v)

