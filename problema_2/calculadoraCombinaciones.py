import time
import sys

def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def calcularCombinacionFormula(n, r):
    if n < 0 or r < 0 or r > n:
        return 0
    factN = factorial(n)
    factR = factorial(r)
    factNR = factorial(n - r)
    return factN // (factR * factNR)

def generarTrianguloPascal(filas):
    triangulo = []
    for n in range(filas + 1):
        fila = [1] * (n + 1)
        for r in range(1, n):
            fila[r] = triangulo[n - 1][r - 1] + triangulo[n - 1][r]
        triangulo.append(fila)
    return triangulo

def mostrarTrianguloEstetico(triangulo):
    max_fila = triangulo[-1]
    ancho_bloque = len(str(max_fila[len(max_fila)//2])) + 1
    ancho_total = len(max_fila) * ancho_bloque * 2

    print("Triángulo de pascal generado")
    
    for i, fila in enumerate(triangulo):
        fila_str = " ".join(f"{num:^{ancho_bloque}}" for num in fila)
        print(f"Fila {i:2d} ➜ {fila_str:^{ancho_total}}")
    print("\n" + "="*40)

def menu():
    while True:
        print("\nCalculadora de Combinaciones y Triángulo de Pascal")
        print("1. Calcular combinación C(n,r) manualmente y verificar simetría")
        print("2. Generar el Triángulo de Pascal estético hasta la fila n")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ").strip()
        
        if opcion == "1":
            try:
                n = int(input("Ingrese el valor de n (total de elementos): "))
                r = int(input("Ingrese el valor de r (elementos a seleccionar): "))

                if n < 0 or r < 0:
                    print("Error: n y r deben ser números enteros no negativos.")
                    continue

                if r > n:
                    print(f"\nCaso especial (r>n): C({n}, {r}) = 0")
                    print(f"No se pueden seleccionar {r} objetos de un conjunto de {n}")
                    continue

                # Fórmula directa
                start_formula = time.perf_counter()
                resultado_formula = calcularCombinacionFormula(n, r)
                end_formula = time.perf_counter()
                tiempo_formula = end_formula - start_formula

                # Triángulo de Pascal 
                start_pascal = time.perf_counter()
                triangulo_temporal = generarTrianguloPascal(n)
                resultado_pascal = triangulo_temporal[n][r]
                end_pascal = time.perf_counter()
                tiempo_pascal = end_pascal - start_pascal

                # Verificación simetría C(n,r) = C(n, n-r)
                resultado_simetrico = calcularCombinacionFormula(n, n - r)

                print(f"\nResultado C({n},{r}) = {resultado_formula}")
                print(f"Tiempo usando Fórmula Directa: {tiempo_formula:.8f} segundos")
                print(f"Tiempo usando Triángulo de Pascal: {tiempo_pascal:.8f} segundos")
                
                print(f"\nVerificación de Identidad Combinatoria:")
                print(f"➜ C({n}, {r}) = {resultado_formula}")
                print(f"➜ C({n}, {n} - {r}) = C({n}, {n-r}) = {resultado_simetrico}")
                
                if resultado_formula == resultado_simetrico:
                    print("¡Identidad verificada con éxito! C(n,r) es exactamente igual a C(n,n-r).")
                else:
                    print("Error en la verificación de la identidad.")

            except ValueError:
                print("Error: Debe ingresar solo números enteros válidos")

        elif opcion == "2":
            try:
                n = int(input("Ingrese el número de la fila máxima de Pascal (n): "))
                if n < 0:
                    print("Error: El número de filas no puede ser negativo.")
                    continue
                
                # Advertencia para triangulos demasiados grandes
                if n > 25:
                    confirmar = input("Un valor de n > 25 puede deformar la visualización en consolas estándar. ¿Desea continuar? (s/n): ").strip().lower()
                    if confirmar != 's':
                        continue

                triangulo = generarTrianguloPascal(n)
                mostrarTrianguloEstetico(triangulo)

            except ValueError:
                print("Error: Debe ingresar un número entero válido")

        elif opcion == "3":
            print("¡Gracias por usar la calculadora del Problema 2! Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo")

if __name__ == "__main__":
    menu()