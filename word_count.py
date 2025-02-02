"""
Módulo para contar la frecuencia de palabras en un archivo de texto.
"""

import sys
import time
from collections import defaultdict

def count_words(filename):
    """Cuenta la frecuencia de cada palabra en un archivo."""
    word_counts = defaultdict(int)
    total_words = 0
    start_time = time.time()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word_counts[word.lower()] += 1
                    total_words += 1
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no se encontró.")
        return
    except (OSError, IOError) as error:
        print(f"Error al procesar el archivo: {error}")
        return
    elapsed_time = time.time() - start_time
    # Guardar resultados en archivo
    output_file = "WordCountResults.txt"
    try:
        with open(output_file, 'w', encoding='utf-8') as out:
            for word, count in sorted(word_counts.items()):
                out.write(f"{word}: {count}\n")
            out.write(f"\nGran Total: {total_words}\n")
            out.write(f"\nTiempo de ejecución: {elapsed_time:.4f} segundos\n")
    except (OSError, IOError) as error:
        print(f"Error al escribir en el archivo de salida: {error}")
    # Imprimir resultados en pantalla
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")
    print(f"\nGran Total: {total_words}")
    print(f"\nTiempo de ejecución: {elapsed_time:.4f} segundos")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python word_count.py fileWithData.txt")
    else:
        count_words(sys.argv[1])
