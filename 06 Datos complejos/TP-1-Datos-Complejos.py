# Ejercicio 1: Agregar frutas y sus precios al diccionario inicial
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agrego más frutas con su precio
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Ejercicio 1 - Frutas agregadas:")
print(precios_frutas)
print()  # Esto es para dejar un espacio visual al imprimir

# Ejercicio 2: Actualizo precios de algunas frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Ejercicio 2 - Precios actualizados:")
print(precios_frutas)
print()

# Ejercicio 3: Crear una lista sólo con los nombres de las frutas (sin precios)
lista_frutas = list(precios_frutas.keys())

print("Ejercicio 3 - Lista con frutas:")
print(lista_frutas)
print()

# Ejercicio 4: Guardar y consultar números telefónicos
contactos = {}

print("Ejercicio 4 - Ingreso de 5 contactos")
for i in range(5):
    nombre = input(f"Ingrese nombre del contacto {i+1}: ")
    telefono = input(f"Ingrese teléfono de {nombre}: ")
    contactos[nombre] = telefono

buscar = input("Ingrese un nombre para buscar el teléfono: ")
if buscar in contactos:
    print(f"El teléfono de {buscar} es {contactos[buscar]}")
else:
    print(f"No se encontró el contacto {buscar}")
print()

# Ejercicio 5: Palabras únicas y cuántas veces aparecen en una frase
frase = input("Ejercicio 5 - Ingrese una frase: ")
palabras = frase.split()

# Conjunto para palabras únicas
palabras_unicas = set(palabras)

# Diccionario para contar frecuencia
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Recuento de palabras:", recuento)
print()

# Ejercicio 6: Promedio de notas de 3 alumnos
alumnos = {}
print("Ejercicio 6 - Ingresar nombres y notas de 3 alumnos")
for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("Promedios por alumno:")
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: {promedio:.2f}")
print()

# Ejercicio 7: Sets de estudiantes que aprobaron dos parciales
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107}

print("Ejercicio 7 - Estudiantes que aprobaron ambos parciales:")
print(parcial1.intersection(parcial2))  # Intersección

print("Estudiantes que aprobaron sólo uno de los dos parciales:")
print(parcial1.symmetric_difference(parcial2))  # Diferencia simétrica

print("Estudiantes que aprobaron al menos un parcial:")
print(parcial1.union(parcial2))  # Unión
print()

# Ejercicio 8: Control de stock
stock = {}

print("Ejercicio 8 - Control de stock")

while True:
    accion = input("Ingrese acción (consultar, agregar, nuevo, salir): ").lower()
    if accion == 'salir':
        break
    elif accion == 'consultar':
        producto = input("Producto a consultar: ")
        if producto in stock:
            print(f"Stock de {producto}: {stock[producto]}")
        else:
            print("Producto no encontrado.")
    elif accion == 'agregar':
        producto = input("Producto para agregar unidades: ")
        if producto in stock:
            cantidad = int(input("Cantidad a agregar: "))
            stock[producto] += cantidad
            print(f"Stock actualizado: {stock[producto]}")
        else:
            print("El producto no existe, usa 'nuevo' para agregar.")
    elif accion == 'nuevo':
        producto = input("Nuevo producto: ")
        cantidad = int(input("Cantidad inicial: "))
        stock[producto] = cantidad
        print(f"Producto {producto} agregado con stock {cantidad}")
    else:
        print("Acción inválida, intente de nuevo.")
print()

# Ejercicio 9: Agenda con tuplas (día, hora)
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

print("Ejercicio 9 - Consulta de agenda")
dia = input("Día: ").lower()
hora = input("Hora (HH:MM): ")
evento = agenda.get((dia, hora), "No hay evento programado para ese día y hora")
print(f"Evento: {evento}")
print()

# Ejercicio 10: Invertir diccionario país-capital
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {capital: pais for pais, capital in original.items()}

print("Ejercicio 10 - Diccionario invertido")
print(invertido)
