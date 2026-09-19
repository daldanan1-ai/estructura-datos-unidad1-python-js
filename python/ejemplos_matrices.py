def main():
    # 1. Declaracion e inicializacion de una matriz 3x3 (valores del 1 al 9)
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    # 2. Recorrido en forma de tabla (por filas)
    print("Matriz en tabla:")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="\t")
        print()

    # 3. Recorrido por columnas
    print("\nRecorrido por columnas:")
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            print(matriz[i][j], end=" ")

    # 4. Suma de todos los elementos
    suma_total = 0
    for fila in matriz:
        for valor in fila:
            suma_total += valor
    print("\n\nSuma total:", suma_total)

    # 5. Intercambiar la primera fila con la ultima
    temp = matriz[0]
    matriz[0] = matriz[len(matriz) - 1]
    matriz[len(matriz) - 1] = temp

    print("\nMatriz despues de intercambiar primera y ultima fila:")
    for fila in matriz:
        for valor in fila:
            print(valor, end="\t")
        print()


if __name__ == "__main__":
    main()
