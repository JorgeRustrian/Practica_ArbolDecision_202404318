from src.data_loader import load_numbers
from src.decision_tree import ejecutar_arbol

def main():
    numeros = load_numbers()
    ejecutar_arbol(numeros)

if __name__ == "__main__":
    main()
