function main() {
  // 1. Declaracion e inicializacion de una matriz 3x3 (valores del 1 al 9)
  const matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ];

  // 2. Recorrido en forma de tabla (por filas)
  console.log("Matriz en tabla:");
  for (let i = 0; i < matriz.length; i++) {
    for (let j = 0; j < matriz[i].length; j++) {
      process.stdout.write(matriz[i][j] + "\t");
    }
    console.log();
  }

  // 3. Recorrido por columnas
  console.log("\nRecorrido por columnas:");
  for (let j = 0; j < matriz[0].length; j++) {
    for (let i = 0; i < matriz.length; i++) {
      process.stdout.write(matriz[i][j] + " ");
    }
  }

  // 4. Suma de todos los elementos
  let sumaTotal = 0;
  for (const fila of matriz) {
    for (const valor of fila) {
      sumaTotal += valor;
    }
  }
  console.log("\n\nSuma total: " + sumaTotal);

  // 5. Intercambiar la primera fila con la ultima
  const temp = matriz[0];
  matriz[0] = matriz[matriz.length - 1];
  matriz[matriz.length - 1] = temp;

  console.log("\nMatriz despues de intercambiar primera y ultima fila:");
  for (const fila of matriz) {
    for (const valor of fila) {
      process.stdout.write(valor + "\t");
    }
    console.log();
  }
}

main();
