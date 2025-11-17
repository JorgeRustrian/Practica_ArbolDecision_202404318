import os

def create_numbers_file(file_path):
    """Escribe 1000 números (del 1 al 1000) en el archivo."""
    with open(file_path, "w") as file:
        for i in range(1, 1001):
            file.write(f"{i}\n")
    print("[INFO] Archivo creado con 1000 números.")


def load_numbers(file_path="./data/numeros_1000.txt"):

    # Verificar si existe
    if not os.path.exists(file_path):
        print(f"[INFO] El archivo '{file_path}' no existe. Creando uno nuevo con 1000 números...")
        create_numbers_file(file_path)

    numeros = []
    try:
        with open(file_path, "r") as file:
            for linea in file:
                linea = linea.strip()
                if linea.isdigit():
                    numeros.append(int(linea))

        print(f"[OK] Archivo '{file_path}' cargado correctamente. Total: {len(numeros)} enteros.")
        return numeros

    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo: {e}")
        return []


if __name__ == "__main__":
    nums = load_numbers()
    print(nums[:10], "...")  


