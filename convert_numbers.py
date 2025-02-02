"""
Módulo para convertir números enteros de un archivo a formato binario y hexadecimal.
"""

import sys
import time

def convert_numbers(filename):
    """
    Convierte enteros de un archivo a formato binario y hexadecimal.

    Args:
        filename (str): El nombre del archivo que contiene los enteros.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            numbers = [line.strip() for line in file]

        start_time = time.time()
        results = []  # Inicializar la lista correctamente

        for number in numbers:
            try:
                num = int(number)
                binary_result = bin(num)[2:] if num >= 0 else "-" + bin(abs(num))[2:]
                hex_result = (
                    hex(num)[2:].upper() if num >= 0 else "-" + hex(abs(num))[2:].upper()
                )
                results.append(
                    f"Decimal: {num}, Binario: {binary_result}, Hexadecimal: {hex_result}"
                )
            except ValueError:
                results.append(f"Error: Entrada inválida '{number}'")

        end_time = time.time()
        elapsed_time = end_time - start_time

        with open('ConvertionResults.txt', 'w', encoding='utf-8') as output_file:
            for result in results:
                print(result)
                output_file.write(result + '\n')

        print(f"Tiempo transcurrido: {elapsed_time:.4f} segundos")

    except FileNotFoundError:
        print(f"Error: Archivo '{filename}' no encontrado.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python convert_numbers.py <filename>")
    else:
        convert_numbers(sys.argv[1])
