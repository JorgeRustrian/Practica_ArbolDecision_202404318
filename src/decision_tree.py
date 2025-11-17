# decision_tree.py
import time

UMBRAL = 50  # valor por defecto

def clasificar_numero(numero, umbral=UMBRAL):
    """Árbol de decisión de un solo nodo:
       numero >= umbral → Alto
       numero <  umbral → Bajo
    """
    return "Alto" if numero >= umbral else "Bajo"


def ejecutar_arbol(lista_numeros, umbral=UMBRAL):
    """Recibe una lista, clasifica y muestra resultados."""
    
    inicio = time.time()

    resultados = []
    altos = 0
    bajos = 0

    for num in lista_numeros:
        clase = clasificar_numero(num, umbral)
        resultados.append(clase)

        if clase == "Alto":
            altos += 1
        else:
            bajos += 1

    # Mostrar primeros 10
    print("\n=== Primeros 10 resultados ===")
    for n, c in zip(lista_numeros[:10], resultados[:10]):
        print(f"{n} → {c}")

    # Conteos
    print("\n=== Conteos ===")
    print(f"Altos: {altos}")
    print(f"Bajos: {bajos}")

    # Tiempo de ejecución
    fin = time.time()
    print(f"\nTiempo total: {fin - inicio:.6f} segundos")

    return resultados, altos, bajos

