#TP 3 - Estructuras Condicionales
#Tecnicatura Universitaria en Programación a Distancia - UTN
#Unidad 3 —Trabajo Práctico Condicionales 
#Asignatura: Programación I
#Alumno: Agustina Cruz
#Matricula: 100652


# ----------------------------------
# Ejercicio 1
# Verifica si la persona es mayor de edad
# ----------------------------------

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


# ----------------------------------
# Ejercicio 2
# Evalúa si la nota está aprobada o desaprobada
# ----------------------------------

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# ----------------------------------
# Ejercicio 3
# Verifica si el número ingresado es par
# ----------------------------------

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# ----------------------------------
# Ejercicio 4
# Clasifica la edad en categorías
# ----------------------------------

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# ----------------------------------
# Ejercicio 5
# Verifica la longitud de una contraseña
# ----------------------------------

contraseña = input("Ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Contraseña válida")
else:
    print("La contraseña debe tener entre 8 y 14 caracteres")


# ----------------------------------
# Ejercicio 6
# Calcula media, mediana y moda, y evalúa sesgo
# ----------------------------------

import random
from statistics import mean, median, mode

numeros = [random.randint(1, 100) for _ in range(50)]

media = mean(numeros)
mediana = median(numeros)
moda = mode(numeros)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")


# ----------------------------------
# Ejercicio 7
# Agrega signo de exclamación si termina en vocal
# ----------------------------------

texto = input("Ingrese una palabra o frase: ")

if texto[-1].lower() in "aeiou":
    print(texto + "!")
else:
    print(texto)


# ----------------------------------
# Ejercicio 8
# Cambia el formato del nombre según opción
# ----------------------------------

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 (MAY), 2 (min), o 3 (Primera May): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")


# ----------------------------------
# Ejercicio 9
# Clasifica la magnitud de un terremoto
# ----------------------------------

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud < 4:
    print("Leve")
elif magnitud < 5:
    print("Moderado")
elif magnitud < 6:
    print("Fuerte")
elif magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")


# ----------------------------------
# Ejercicio 10
# Determina la estación del año según fecha y hemisferio
# ----------------------------------

hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el número de mes (1-12): "))
dia = int(input("Ingrese el día: "))

if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
else:
    estacion = "Otoño" if hemisferio == "N" else "Primavera"

print("Estación:", estacion)