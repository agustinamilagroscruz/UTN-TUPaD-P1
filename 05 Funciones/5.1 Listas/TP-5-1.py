# Ejercicio 1: Crear una lista con múltiplos de 4 del 1 al 100
multiplos_de_4 = list(range(4, 101, 4))  # range desde 4 hasta 100 saltando de 4 en 4
print(multiplos_de_4)  # Imprime la lista con todos los múltiplos de 4

# Ejercicio 2: Mostrar el penúltimo elemento de una lista con 5 elementos
cosas_favoritas = ["chocolate", "gatos", "python", "música", "pizza"]
print(cosas_favoritas[-2])  # Índice -2 accede al penúltimo elemento ("música")

# Ejercicio 3: Crear lista vacía y agregar palabras con append
lista_vacia = []  # Lista inicial vacía
lista_vacia.append("sol")     # Agrega "sol"
lista_vacia.append("luna")    # Agrega "luna"
lista_vacia.append("estrella")# Agrega "estrella"
print(lista_vacia)  # Imprime la lista resultante

# Ejercicio 4: Reemplazar elementos en la lista animales
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"    # Cambia el segundo elemento "gato" por "loro"
animales[-1] = "oso"    # Cambia el último elemento "pez" por "oso"
print(animales)         # Imprime la lista modificada

# Ejercicio 5: Eliminar el número más grande de la lista
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))  # max(numeros) devuelve 22, que se elimina con remove()
print(numeros)                # Imprime la lista sin el número más grande

# Ejercicio 6: Crear lista del 10 al 30 con saltos de 5 y mostrar primeros dos elementos
numeros = list(range(10, 31, 5))  # Lista con números 10, 15, 20, 25, 30
print(numeros[:2])                # Imprime los primeros dos elementos: 10 y 15

# Ejercicio 7: Reemplazar valores centrales de la lista autos
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["civic", "focus"]  # Reemplaza el segundo y tercer elemento
print(autos)                     # Imprime la lista modificada

# Ejercicio 8: Crear lista con dobles de 5, 10 y 15 usando append
dobles = []
dobles.append(5 * 2)   # Agrega 10
dobles.append(10 * 2)  # Agrega 20
dobles.append(15 * 2)  # Agrega 30
print(dobles)          # Imprime la lista con los dobles

# Ejercicio 9: Modificar lista anidada compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")        # Agrega "jugo" al tercer cliente
compras[1][1] = "tallarines"     # Reemplaza "fideos" por "tallarines"
compras[0].remove("pan")          # Elimina "pan" del primer cliente

print(compras)  # Imprime la lista anidada modificada

# 1Ejercicio 10: Crear lista anidada con diferentes tipos
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)  # Imprime la lista con enteros, booleanos y lista interna
