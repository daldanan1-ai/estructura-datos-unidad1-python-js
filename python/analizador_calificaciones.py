def leer_entero(mensaje):
    """Lee un entero; si el usuario escribe otra cosa, lo vuelve a pedir."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            mensaje = "Entrada invalida. Ingrese un numero entero: "


def leer_decimal(mensaje):
    """Lee un decimal; si el usuario escribe otra cosa, lo vuelve a pedir."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            mensaje = "Entrada invalida. Ingrese un numero: "


def main():
    n = leer_entero("Ingrese el numero de calificaciones (N): ")

    if n <= 0:
        print("El numero de calificaciones debe ser mayor a 0.")
        return

    calificaciones = [0.0] * n
    aprobados = 0
    reprobados = 0
    suma = 0.0

    # Lectura y validacion (0 - 100)
    for i in range(n):
        while True:
            cal = leer_decimal(f"Ingrese la calificacion {i + 1} (0-100): ")
            if 0 <= cal <= 100:
                calificaciones[i] = cal
                suma += cal
                if cal >= 60:  # Criterio: Aprobado >= 60
                    aprobados += 1
                else:
                    reprobados += 1
                break
            else:
                print("Error. Ingrese entre 0 y 100.")

    # Calculo del promedio
    promedio = suma / n

    # Copia y ordenamiento para calcular mediana y moda
    ordenadas = calificaciones.copy()
    ordenadas.sort()

    # Calculo de la mediana
    mitad = n // 2
    if n % 2 == 0:
        mediana = (ordenadas[mitad - 1] + ordenadas[mitad]) / 2
    else:
        mediana = ordenadas[mitad]

    # Calculo de la moda
    moda = ordenadas[0]
    max_frec = 0
    for i in range(n):
        frec = 0
        for j in range(n):
            if ordenadas[j] == ordenadas[i]:
                frec += 1
        if frec > max_frec:
            max_frec = frec
            moda = ordenadas[i]

    # Histograma de frecuencias
    rangos = [0] * 5  # 0-20, 21-40, 41-60, 61-80, 81-100
    for cal in calificaciones:
        if cal <= 20:
            rangos[0] += 1
        elif cal <= 40:
            rangos[1] += 1
        elif cal <= 60:
            rangos[2] += 1
        elif cal <= 80:
            rangos[3] += 1
        else:
            rangos[4] += 1

    print("\n--- RESULTADOS ESTADISTICOS ---")
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda:.2f}")
    print(f"Aprobados: {aprobados} ({aprobados / n * 100:.1f}%)")
    print(f"Reprobados: {reprobados} ({reprobados / n * 100:.1f}%)")

    print("\n--- HISTOGRAMA ---")
    etiquetas = ["0-20: ", "21-40: ", "41-60: ", "61-80: ", "81-100: "]
    for i in range(5):
        print(etiquetas[i], end="\t")
        for _ in range(rangos[i]):
            print("*", end="")
        print(f" ({rangos[i]})")


if __name__ == "__main__":
    main()
