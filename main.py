from src.data_loader import load_numbers
from src.decision_tree import ejecutar_arbol

def main():
    valor = input("Ingrese el umbral (ENTER para usar 50): ")

   
   
    if valor.strip() == "":
        umbral = 50
    else:
        umbral = int(valor)

    numeros = load_numbers()
    ejecutar_arbol(numeros, umbral)


if __name__ == "__main__":
    main()
