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

    print("\n--- RESULTADOS ESTADISTICOS ---")
    print(f"Promedio: {promedio:.2f}")
    print(f"Aprobados: {aprobados} ({aprobados / n * 100:.1f}%)")
    print(f"Reprobados: {reprobados} ({reprobados / n * 100:.1f}%)")


if __name__ == "__main__":
    main()
