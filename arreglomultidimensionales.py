def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, i, j
    return False, -1, -1

# Matriz de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

valor_buscado = 5
encontrado, fila, columna = buscar_valor(matriz, valor_buscado)

if encontrado:
    print(f"El valor {valor_buscado} se encontró en la fila {fila+1}, columna {columna+1}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")


    def ordenar_fila(matriz, fila):
        matriz[fila - 1] = sorted(matriz[fila - 1])


    # Matriz de ejemplo
    matriz = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    fila_a_ordenar = 2
    print("Matriz original:")
    for row in matriz:
        print(row)

    ordenar_fila(matriz, fila_a_ordenar)

    print("\nMatriz con la fila ordenada:")
    for row in matriz:
        print(row)