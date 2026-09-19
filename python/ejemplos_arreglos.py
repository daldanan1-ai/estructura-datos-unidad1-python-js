import random


def imprimir(arreglo):
    for valor in arreglo:
        print(valor, end=" ")
    print()


def busqueda_lineal(arreglo, valor_buscado):
    """Devuelve la posicion de la primera coincidencia o -1 si no existe."""
    for i in range(len(arreglo)):
        if arreglo[i] == valor_buscado:
            return i
    return -1


def buscar(arreglo, valor_buscado):
    pos = busqueda_lineal(arreglo, valor_buscado)
    if pos != -1:
        print(f"\nValor {valor_buscado} encontrado en el indice {pos}")
    else:
        print(f"\nValor {valor_buscado} no encontrado.")


def main():
    # 1. Declaracion y creacion de un arreglo de 10 enteros (10 posiciones en 0)
    numeros = [0] * 10

    # 2. Inicializacion con valores aleatorios (1 a 100)
    for i in range(len(numeros)):
        numeros[i] = random.randint(1, 100)

    # 3. Recorrido con for clasico (por indice)
    print("Arreglo (for clasico):")
    for i in range(len(numeros)):
        print(numeros[i], end=" ")

    # 4. Recorrido con for-each (por valor)
    print("\n\nArreglo (for-each):")
    for num in numeros:
        print(num, end=" ")

    # 5. Modificacion (a): impares a cero
    for i in range(len(numeros)):
        if numeros[i] % 2 != 0:
            numeros[i] = 0
    print("\n\nDespues de cambiar impares por 0:")
    imprimir(numeros)

    # 5. Modificacion (b): multiplicar cada valor por su indice
    for i in range(len(numeros)):
        numeros[i] = numeros[i] * i
    print("\nDespues de multiplicar por el indice:")
    imprimir(numeros)

    # 6. Busqueda lineal
    buscar(numeros, 0)   # siempre esta: numeros[0] * 0 = 0
    buscar(numeros, 15)  # nunca esta: 15 es impar y habria quedado en 0


if __name__ == "__main__":
    main()
