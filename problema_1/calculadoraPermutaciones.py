import time
import sys

def factorialPorIteracion(n):
    resultado=1
    for i in range(2, n+1):
        resultado*=i
    return resultado

def factorialPorRecursion(n):
    if n==0 or n==1: return 1
    return n*factorialPorRecursion(n-1)

def calcularPermutacion(n, r, usarRecursion=False):
    if n<0 or r<0:
        return None, None
    
    if r>n:
        return 0, 0
    
    if usarRecursion:
        if n>900: sys.setrecursionlimit(n+100)
        start=time.perf_counter()
        factN=factorialPorRecursion(n)
        factNR=factorialPorRecursion(n-r)
        end=time.perf_counter()

    else:
        start=time.perf_counter()
        factN=factorialPorIteracion(n)
        factNR=factorialPorIteracion(n-r)
        end=time.perf_counter()

    resultado=factN//factNR
    tiempo= end-start
    
    return resultado, tiempo

def ejecutarPruebasAutomaticas():
    print("A continuación se ejecutaran cinco pruebas con diferentes valores de entrada:")

    casosParaPruebas=[
        (10,3, "Caso ejemplo guía"),
        (20,5, "Caso ejemplo guía"),
        (5,5, "Caso Especial r=n"),
        (10,0, "Caso Especial r=0"),
        (5,8, "Caso Especial r>n")
    ]

    for i, (n, r, desc) in enumerate(casosParaPruebas, 1):
        print(f"\nPrueba #{i}: {desc}")
        print(f"Entradas: n = {n}, r = {r}")

        if r>n:
            print(f"Caso especial (r>n): P({n}, {r}) = 0")
            print(f"No se pueden ordenar {r} objetos de un conjunto de {n}")
            print(f"Tiempo usando la iteración: 0.00000000 s \nTiempo usando la recursión: 0.00000000 s\n")
            continue
        
        resultadoIteracion, tiempoIteracion=calcularPermutacion(n, r, usarRecursion=False) 
        _, tiempoRecursion=calcularPermutacion(n, r, usarRecursion=True)

        print(f"Resultado: P({n},{r})={resultadoIteracion}")
        print(f"Tiempo usando la iteración: {tiempoIteracion:.8f} s \nTiempo usando la recursión: {tiempoRecursion:.8f} s\n")


def menu():
    while True:
        print("\nCalculadora general de permutaciones P(n,r)")
        print("1. Calcular una permutación manualmente")
        print("2. Ejecutar los 5 casos de prueba obligatorios (Comparar tiempos)")
        print("3. Salir")

        opcion=input("Seleccione una opción (1-3): ")
        if opcion=="1":
            try:
                n=int(input("Ingrese el valor de n (total de elementos): "))
                r=int(input("Ingrese el valor de r (elementos a ordenar): "))

                if n < 0 or r < 0:
                    print("Error: n y r deben ser números enteros no negativos.")
                    continue

                if r > n:
                    print(f"\nCaso especial (r>n): P({n}, {r}) = 0")
                    print(f"No se pueden ordenar {r} objetos de un conjunto de {n}")
                    print(f"⏱️ Tiempo de procesamiento: 0.00000000 segundos")
                    continue

                while True:
                    print("\nSeleccione el método para realizar el cálculo:")
                    print("a. Usando iteración")
                    print("b. Usando recursividad")
                    metodoSeleccionado = input("Opción (a o b): ").strip().lower()
                    
                    if metodoSeleccionado in ["a", "b"]:
                        break
                    else:
                        print("\nOpción inválida. Ingrese únicamente 'a' o 'b'")

                esRecursion = (metodoSeleccionado == "b")
                resultado1, tiempo1 = calcularPermutacion(n, r, esRecursion)

                if resultado1 is not None:
                    print(f"\nResultado: P({n},{r})={resultado1}")
                    print(f"Tiempo de procesamiento: {tiempo1:.8f} segundos")
            
            except ValueError:
                print("Error: Debe ingresar solo número enteros válidos")

        elif opcion=="2":
            ejecutarPruebasAutomaticas()

        elif opcion=="3":
            print("Saliendo")
            break

        else:
            print("Opción inválida. Intente de nuevo")

if __name__=="__main__":
    menu()