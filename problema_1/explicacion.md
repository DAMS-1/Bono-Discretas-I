# Problema 1: Calculadora General de Permutaciones y k-Permutaciones

## 1. Explicación del Problema de Conteo
El problema consiste en determinar el número de formas en que se pueden ordenar un subconjunto de $r$ elementos tomados a partir de un conjunto inicial de $n$ elementos distintos.

En este caso de conteo, el orden en el que se seleccionan y posicionan los objetos sí importa. Por ejemplo, si tenemos el conjunto $\{A, B, C\}$ y queremos ordenar 2 elementos, la forma $(A, B)$ se cuenta como una opción completamente diferente a $(B, A)$.

## 2. Principio combinatorio Usado y su fórmula
Para construir esta herramienta general utilice el principio multiplicativo/regla del producto. Para ubicar el primer objeto dispuse de $n$ opciones; entonces para el segundo quedan $(n-1)$ opciones, y así sucesivamente hasta llegar al objeto número $r$, que tendrá $(n-r+1)$ opciones disponibles.

Al multiplicar estas opciones obtuve la fórmula matemática compacta de las k-permutaciones:

$$P(n, r) = \frac{n!}{(n - r)!}$$

Donde:
* $n!$ representa el factorial de $n$, es decir, el total de formas de ordenar los $n$ objetos del conjunto completo.
* $(n-r)!$ representa las permutaciones de los objetos restantes que **no** fueron seleccionados, dividiendo por este valor para "cancelar" las posiciones que no nos interesan.

## 3. Casos Especiales y Validaciones del Modelo
Implemente las siguientes restricciones para que el modelo tenga sentido y no presente fallas
1.  **No negatividad:** Tanto $n$ como $r$ deben ser enteros no negativos ($n \ge 0, r \ge 0$). 
2.  **Tamaño del subconjunto:** Debe cumplirse que $r \le n$. Si un usuario intenta ordenar más objetos de los que tiene disponibles ($r > n$), el resultado matemático es de forma inmediata $0$, debido a que es un evento imposible.
3.  **Caso Base ($r = 0$):** Si se desea ordenar $0$ objetos de un conjunto de $n$, existe exactamente $1$ sola forma de hacerlo (la forma vacía). La fórmula responde correctamente ya que $P(n,0) = \frac{n!}{n!} = 1$.

## 4. Eficiencia del Algoritmo
* **Enfoque Iterativo:** El cálculo del factorial mediante ciclos tradicionales tiene una complejidad temporal de $O(n)$, ya que realiza exactamente $n-1$ multiplicaciones. Su uso de memoria es óptimo, con una complejidad espacial de $O(1)$.
* **Enfoque Recursivo:** Computacionalmente, cada llamado recursivo de la función añade un nuevo marco a la pila de llamadas (*Call Stack*). Esto implica una complejidad espacial de $O(n)$, lo que genera un riesgo latente de desbordamiento de pila (*Stack Overflow*) si $n$ toma valores muy elevados.

