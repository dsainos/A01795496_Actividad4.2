"""
Modulo para calcular estadisticas descriptivas de un conjunto de numeros.
"""

import sys
import time
import re
from decimal import Decimal, getcontext, ROUND_HALF_UP

def compute_stats(data_list):
    """Calcula las estadísticas descriptivas de una lista de números."""
    n = len(data_list)
    if n == 0:
        return {
            'media': None,
            'mediana': None,
            'moda': "#N/A",
            'desviacion_estandar': None,
            'varianza': None
        }

    # Calcula la media
    media = sum(data_list) / n
    media = media.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)  # Redondeo a 2 decimales

    # Calcula la mediana
    data_ordenada = sorted(data_list)
    if n % 2 == 0:
        mediana = (data_ordenada[n // 2 - 1] + data_ordenada[n // 2]) / Decimal(2)
    else:
        mediana = data_ordenada[n // 2]

    # Calcula la moda
    frecuencias = {}
    for num in data_list:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    moda = max(frecuencias, key=frecuencias.get) if max(frecuencias.values()) > 1 else "#N/A"

    # Calcula la desviación estándar y la varianza
    suma_cuadrados = sum((x - media) ** 2 for x in data_list)
    varianza = suma_cuadrados / (n - 1) if n > 1 else Decimal(0)
    desviacion_estandar = varianza.sqrt() if varianza > 0 else Decimal(0)

    # Redondeo de los resultados finales
    varianza = varianza.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    desviacion_estandar = desviacion_estandar.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    return {
        'media': media,
        'mediana': mediana,
        'moda': moda,
        'desviacion_estandar': desviacion_estandar,
        'varianza': varianza
    }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python compute_statistics.py <archivo_datos.txt>")
        sys.exit(1)

    ARCHIVO_ENTRADA = sys.argv[1]

    # Configurar la precisión de Decimal
    getcontext().prec = 50  # 50 dígitos de precisión en cálculos

    try:
        with open(ARCHIVO_ENTRADA, 'r', encoding='utf-8') as archivo:
            datos = []
            NUM_REGISTROS = 0
            for linea in archivo:
                linea_limpia = linea.strip()

                # Extraer solo la parte numérica (ignorar letras y símbolos extra)
                match = re.search(r"-?\d+(\.\d+)?", linea_limpia)
                if match:
                    numero = Decimal(match.group())  # Convertir solo el número encontrado
                    datos.append(numero)
                NUM_REGISTROS += 1  # Contar todas las líneas, incluso si no tienen números

    except FileNotFoundError:
        print(f"Error: Archivo no encontrado: {ARCHIVO_ENTRADA}")
        sys.exit(1)

    print(f"Número de registros leídos: {NUM_REGISTROS}")

    inicio = time.time()
    estadisticas = compute_stats(datos)
    fin = time.time()
    tiempo_transcurrido = fin - inicio

    print("Resultados:")
    for clave, valor in estadisticas.items():
        print(f"{clave}: {valor}")
    print(f"Tiempo transcurrido: {tiempo_transcurrido:.4f} segundos")

    with open('StatisticsResults.txt', 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.write(f"Número de registros leídos: {NUM_REGISTROS}\n")
        archivo_salida.write("Resultados:\n")
        for clave, valor in estadisticas.items():
            archivo_salida.write(f"{clave}: {valor}\n")
        archivo_salida.write(f"Tiempo transcurrido: {tiempo_transcurrido:.4f} segundos\n")
