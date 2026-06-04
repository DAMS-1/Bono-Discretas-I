# Problema 2: Combinaciones y Triángulo de Pascal

## 1. Sustento Matemático

### Definición de Combinación
Una combinación es la selección de un subconjunto de $r$ elementos tomados de un conjunto mayor de $n$ elementos disponibles, en este caso el orden de los elementos no importa. 

El número de combinaciones posibles se denota como $C(n, r)$ o mediante el coeficiente binomial $\binom{n}{r}$, y su fórmula explícita es:

$$\binom{n}{r} = \frac{n!}{r! \cdot (n - r)!}$$

Donde:
* $n!$ es el total de formas de ordenar el conjunto completo.
* $r!$ elimina las redundancias generadas por los diferentes ordenamientos de los elementos seleccionados (ya que el orden no importa).
* $(n - r)!$ elimina las formas de ordenar los elementos que no fueron seleccionados.

## 2. Demostración Formal de la Identidad Combinatoria

Debo demostrar analíticamente que:

$$\binom{n}{r} = \binom{n}{n - r}$$

### Demostración por Definición Algebraica:

1. A partir de la definición del coeficiente binomial, sabemos que el lado izquierdo de la ecuación es:
   $$\binom{n}{r} = \frac{n!}{r! \cdot (n - r)!}$$

2. Aplique la misma definición para el lado derecho de la ecuación, sustituyendo formalmente la variable "$r$" por la expresión "$(n - r)$":
   $$\binom{n}{n - r} = \frac{n!}{(n - r)! \cdot [n - (n - r)]!}$$

3. Simplifique el argumento dentro del segundo factorial del denominador aplicando la ley de signos:
   $$n - (n - r) = n - n + r = r$$

4. Sustituyendo esta simplificación en la ecuación del paso 2, obtuve:
   $$\binom{n}{n - r} = \frac{n!}{(n - r)! \cdot r!}$$

5. Por la propiedad conmutativa de la multiplicación en los números enteros, puedo afirmar que $(n - r)! \cdot r! = r! \cdot (n - r)!$. Al reordenar el denominador obtuve:
   $$\binom{n}{n - r} = \frac{n!}{r! \cdot (n - r)!}$$

6. Al comparar ambos resultados, puedo afirmar que:
   $$\frac{n!}{r! \cdot (n - r)!} = \frac{n!}{r! \cdot (n - r)!} \implies \binom{n}{r} = \binom{n}{n - r}$$

**Interpretación combinatoria:** Esta identidad demuestra una simetría perfecta. Elegir $r$ objetos para formar un subconjunto es exactamente equivalente a elegir los $(n - r)$ objetos que se van a quedar por fuera del subconjunto.


## 3. Relación con el Triángulo de Pascal

El Triángulo de Pascal es una representación geométrica de los coeficientes binomiales de una forma triangular. Cada fila del triángulo (empezando desde la fila $n = 0$) corresponde a los coeficientes del desarrollo del binomio de Newton $(a + b)^n$.

La posición $r$ en la fila $n$ del triángulo equivale exactamente al valor de $\binom{n}{r}$. 



### Propiedades clave aplicadas al algoritmo:
1.  **Caso Base:** Los extremos de cada fila siempre son iguales a $1$, ya que $\binom{n}{0} = 1$ y $\binom{n}{n} = 1$.
2.  **Relación de Recurrencia (Regla de Pascal):** Cualquier elemento interior del triángulo se calcula sumando los dos elementos que tiene directamente encima en la fila anterior:
    $$\binom{n}{r} = \binom{n - 1}{r - 1} + \binom{n - 1}{r}$$

Esta última propiedad me permite construir la versión óptima del código sin necesidad de calcular factoriales gigantescos, previniendo el desbordamiento de memoria.