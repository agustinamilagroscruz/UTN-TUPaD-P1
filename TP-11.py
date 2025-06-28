
# Ejercicio 1 - Factorial recursivo

def factorial(n):
    # Caso base: factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

numero = int(input("Ej 1 - Ingresá un número entero positivo: "))
print(f"\nFactoriales del 1 al {numero}:\n")
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}")

# Ejercicio 2 - Fibonacci recursivo

def fibonacci(pos):
    # Casos base para las primeras posiciones de Fibonacci
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    # Caso recursivo: suma de los dos valores anteriores
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

n = int(input("\nEj 2 - Hasta qué posición de Fibonacci querés ver? "))
print(f"\nSerie de Fibonacci hasta la posición {n}:\n")
for i in range(n + 1):
    print(f"F({i}) = {fibonacci(i)}")

# Ejercicio 3 - Potencia recursiva

def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: base * potencia(base, exponente-1)
    else:
        return base * potencia(base, exponente - 1)

base = int(input("\nEj 3 - Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))
resultado = potencia(base, exponente)
print(f"\n{base}^{exponente} = {resultado}")


# Ejercicio 4 - Decimal a binario recursivo

def decimal_a_binario(n):
    # Caso base: si n es 0, retorno cadena vacía para formar resultado desde abajo hacia arriba
    if n == 0:
        return ""
    # Recursión: divido por 2 y guardo el resto como string concatenado al resultado recursivo
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("\nEj 4 - Ingresá un número entero en base decimal: "))
if numero == 0:
    print("El número binario es: 0")  # Caso especial para 0
else:
    binario = decimal_a_binario(numero)
    print(f"El número binario es: {binario}")


# Ejercicio 5 - Verificar palíndromo recursivo

def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letras, es palíndromo
    if len(palabra) <= 1:
        return True
    # Si las primeras y últimas letras coinciden, verifico recursivamente el substring interior
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

texto = input("\nEj 5 - Ingresá una palabra sin espacios ni tildes: ").lower()
if es_palindromo(texto):
    print("La palabra ES un palíndromo.")
else:
    print("La palabra NO es un palíndromo.")

# Ejercicio 6 - Suma de dígitos recursiva

def suma_digitos(n):
    # Caso base: si n es menor que 10, retorno n (único dígito)
    if n < 10:
        return n
    # Suma el último dígito (n % 10) más la suma de los dígitos restantes (n // 10)
    else:
        return n % 10 + suma_digitos(n // 10)

numero = int(input("\nEj 6 - Ingresá un número entero positivo: "))
print(f"La suma de sus dígitos es: {suma_digitos(numero)}")


# Ejercicio 7 - Contar bloques pirámide recursivo

def contar_bloques(n):
    # Caso base: si solo queda 1 bloque, retorno 1
    if n == 1:
        return 1
    # Sumo bloques del nivel actual (n) más los bloques de niveles superiores
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("\nEj 7 - ¿Cuántos bloques tiene la base de la pirámide? "))
print(f"Cantidad total de bloques: {contar_bloques(niveles)}")

# Ejercicio 8 - Contar ocurrencias de dígito recursivo

def contar_digito(numero, digito):
    # Caso base: si ya no quedan más dígitos, retorno 0
    if numero == 0:
        return 0
    # Si último dígito es igual al buscado, sumo 1 + resultado recursivo
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    # Si no coincide, solo continuo la recursión sin sumar
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("\nEj 8 - Ingresá un número entero positivo: "))
digito = int(input("¿Qué dígito querés contar (0 a 9)? "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")


