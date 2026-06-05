# Bono de Programación - Matemáticas Discretas I
**Universidad Nacional de Colombia**
**Docente:** Jhoan Sebastian Tenjo García

---

Este repositorio contiene la solución al Bono Programable. En este se implementan, analizan y documentan algoritmos eficientes en Python para el cálculo de estructuras combinatorias fundamentales (Permutaciones y Combinaciones), evaluando enfoques iterativos, recursivos y aditivos mediante la programación dinámica.

---

## Estructura del Repositorio

El proyecto se encuentra estructurado de manera modular con los siguientes directorios:

* **`problema_1/` (Permutaciones)**
    * `calculadoraPermutaciones.py`: Código fuente modular con un menú interactivo que calcula permutaciones $P(n,r)$ tanto por el método iterativo como por el recursivo, aislando la lógica matemática de la interfaz.
    * `pruebas/evidenciaPruebas.txt`: Registro detallado de la salida en consola que valida el correcto funcionamiento de los 5 casos de prueba obligatorios (incluyendo los escenarios especiales $r=n$, $r=0$ y el caso imposible $r>n$).
* **`problema_2/` (Combinaciones y Pascal)**
    * `calculadoraCombinaciones.py`: Código fuente para el cálculo de combinaciones $C(n,r)$ empleando dos enfoques: la fórmula directa por factoriales y la relación de recurrencia aditiva de Pascal. Incluye la extensión opcional para renderizar el triángulo de forma geométrica y centrada.
    * `explicacion.md`: Documentación matemática formal que detalla el sustento teórico, la demostración algebraica de la identidad de simetría $\binom{n}{r} = \binom{n}{n-r}$ y las propiedades de recurrencia aplicadas.
    * `pruebas/evidenciaPruebas.txt`: Registro de ejecución de la terminal que evidencia el cálculo manual, la comprobación automática de la simetría y el Triángulo de Pascal completamente alineado hasta la fila 12.

---

## Requisitos e Instalación

El proyecto fue desarrollado utilizando Python 3. No requiere la instalación de librerías ni dependencias de terceros, ya que hace uso exclusivo de los módulos nativos de la biblioteca estándar de Python (`time` y `sys`).

### Clonar el repositorio
Para replicar o evaluar este proyecto de forma local, ejecuta los siguientes comandos en tu terminal de Git Bash:
```bash
git clone https://github.com/DAMS-1/Bono-Discretas-I.git
cd Bono-Discretas-I
```
--- 

## Instrucciones de Ejecución

### 1. Ejecutar el problema 1: Calculadora de Permutaciones
Para correr el menú interactivo de permutaciones y comprobar la comparativa de alta fidelidad entre tiempos de ejecución, usa:

```bash
python problema_1/calculadoraPermutaciones.py
```

### 2. Ejecutar el problema 2: Calculadora de Combinaciones y Pascal
Para iniciar el entorno interactivo de combinaciones, validar la identidad simétrica o generar geométricamente el Triángulo de Pascal, usa:

```bash
python problema_2/calculadoraCombinaciones.py
```

## Conclusiones del Análisis de Rendimiento

Estabilidad Algorítmica (Permutaciones): El enfoque iterativo demostró ser el más robusto para valores elevados de $n$. Al basarse en un ciclo clásico en lugar de llamadas anidadas, elude la restricción de profundidad de la pila de Python (RecursionError), garantizando la estabilidad del software sin sobrecargar la memoria stack.

Optimización por Programación Dinámica (Combinaciones): La generación de subconjuntos mediante el Triángulo de Pascal demostró las ventajas de la relación aditiva $\binom{n}{r}=\binom{n-1}{r-1}+\binom{n-1}{r}$. Al construir las filas sumando los valores inmediatamente superiores, el algoritmo prescinde por completo del cálculo de factoriales masivos, minimizando drásticamente la carga de operaciones en la CPU.