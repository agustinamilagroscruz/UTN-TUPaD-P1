# Trabajo Práctico 4 - Estructuras Repetitivas
# Nombre: Agustina Cruz
# Materia: Programacion I

# Ejercicio 1: Mostrar los números del 0 al 100
print("Ejercicio 1")
for i in range(101):
    print(i)

    # Ejercicio 2: Contar la cantidad de dígitos de un número ingresado
print("\nEjercicio 2")
num = int(input("Ingrese un número entero: "))
print("Cantidad de dígitos:", len(str(abs(num))))

# Ejercicio 3: Sumar los números entre dos valores dados, excluyendo extremos
print("\nEjercicio 3")
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
inicio = min(a, b) + 1
fin = max(a, b)
suma = 0
for i in range(inicio, fin):
    suma += i
print("Suma entre los dos valores (excluyendo):", suma)

# Ejercicio 4: Sumar números ingresados hasta que se ingrese un 0
print("\nEjercicio 4")
total = 0
while True:
    n = int(input("Ingrese un número (0 para salir): "))
    if n == 0:
        break
    total += n
print("Suma total:", total)

# Ejercicio 5: Juego de adivinanza de número aleatorio
print("\nEjercicio 5")
import random
secreto = random.randint(0, 9)
intentos = 0
while True:
    adivina = int(input("Adivine el número (entre 0 y 9): "))
    intentos += 1
    if adivina == secreto:
        print("¡Correcto! Lo lograste en", intentos, "intentos.")
        break
    else:
        print("Incorrecto, intenta nuevamente.")

        # Ejercicio 6: Mostrar los números pares entre 0 y 100 en orden decreciente
print("\nEjercicio 6")
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

        # Ejercicio 7: Sumar desde 0 hasta un número ingresado
print("\nEjercicio 7")
limite = int(input("Ingrese un número positivo: "))
suma = 0
for i in range(limite + 1):
    suma += i
print("Suma desde 0 hasta", limite, "es:", suma)

# Ejercicio 8: Contar pares, impares, negativos y positivos en 100 números
print("\nEjercicio 8")
pares = impares = positivos = negativos = 0
cantidad = 100  # cambiar este valor a un número menor para pruebas
for _ in range(cantidad):
    n = int(input("Ingrese un número: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n >= 0:
        positivos += 1
    else:
        negativos += 1
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# Ejercicio 9: Calcular la media de 100 números
print("\nEjercicio 9")
suma = 0
cantidad = 100  # cambiar este valor a un número menor para pruebas
for _ in range(cantidad):
    n = int(input("Ingrese un número: "))
    suma += n
media = suma / cantidad
print("Media:", media)

# Ejercicio 10: Invertir los dígitos de un número
print("\nEjercicio 10")
numero = input("Ingrese un número: ")
invertido = numero[::-1]
print("Número invertido:", invertido)