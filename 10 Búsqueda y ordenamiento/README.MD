Link del video a youtube: https://youtu.be/BQmNQFKR354?si=QU5ENSD8f7s3Hj14

1. Introducción Este informe presenta el análisis de dos algoritmos fundamentales: ordenamiento por burbuja (Bubble Sort) y búsqueda por interpolación. El objetivo fue evaluar su funcionamiento y rendimiento en listas de diferentes tamaños.

2. Metodología Se implementaron ambos algoritmos en Python, midiendo los tiempos de ejecución utilizando el módulo time.

2.1 Algoritmo de Ordenamiento Nombre: Bubble Sort

Descripción: Ordena la lista comparando elementos adyacentes e intercambiándolos si están en orden incorrecto.

Complejidad: O(n²)

2.2 Algoritmo de Búsqueda Nombre: Búsqueda por Interpolación

Descripción: Estima la posición del elemento a buscar usando una fórmula matemática que aprovecha la distribución uniforme de los datos.

Condición: Requiere una lista previamente ordenada.

Complejidad (mejor caso): O(log log n)

3. Pruebas Realizadas Se realizaron dos pruebas utilizando listas de diferentes tamaños para evaluar el rendimiento de ambos algoritmos:

Prueba 1: Lista de 100 elementos (ordenada en orden descendente).

Prueba 2: Lista de 10.000 elementos (ordenada en orden descendente).

En ambas pruebas se aplicó primero el ordenamiento por burbuja y luego la búsqueda por interpolación para encontrar un valor presente en la lista.

4. Resultados Obtenidos El ordenamiento por burbuja funcionó correctamente, aunque presentó un tiempo de ejecución considerablemente alto en la lista de 10.000 elementos.

La búsqueda por interpolación fue eficiente en ambos casos, demostrando su efectividad cuando la lista está correctamente ordenada.

Las diferencias de rendimiento fueron evidentes, especialmente con listas grandes: la búsqueda fue casi instantánea, mientras que el ordenamiento tardó varios segundos.

5. Conclusiones Ambos algoritmos funcionan correctamente y cumplen su objetivo.

El ordenamiento por burbuja es útil para listas pequeñas, pero no es recomendable en contextos donde se necesita rendimiento.

La búsqueda por interpolación es altamente eficiente, siempre que se respeten sus condiciones de uso (lista ordenada y distribución relativamente uniforme).

Este trabajo pone en evidencia la importancia de seleccionar el algoritmo adecuado según el tamaño de los datos y el problema a resolver.