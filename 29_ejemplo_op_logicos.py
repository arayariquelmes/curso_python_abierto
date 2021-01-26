#Ejemplo donde se solicita promedio de notas y asistencia de un estudiante
#y determina si en inacap aprueba la asignatura o reprueba

prom = float(input("Ingrese promedio de notas:"))
pa = int(input("Ingrese porcentaje de asistencia:"))
trabajador = input("Es alumno trabajador?")

if (prom >= 3.95 and pa >= 70) or (prom >=3.95 and pa >=50  and trabajador=="si"):
    print("Asignatura aprobada")
else:
    print("Asignatura reprobada")
