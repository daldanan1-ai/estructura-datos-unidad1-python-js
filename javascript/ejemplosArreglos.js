function imprimir(arreglo) {
  for (const valor of arreglo) {
    process.stdout.write(valor + " ");
  }
  console.log();
}

/** Devuelve la posicion de la primera coincidencia o -1 si no existe. */
function busquedaLineal(arreglo, valorBuscado) {
  for (let i = 0; i < arreglo.length; i++) {
    if (arreglo[i] === valorBuscado) {
      return i;
    }
  }
  return -1;
}

function buscar(arreglo, valorBuscado) {
  const pos = busquedaLineal(arreglo, valorBuscado);
  if (pos !== -1) {
    console.log(`\nValor ${valorBuscado} encontrado en el indice ${pos}`);
  } else {
    console.log(`\nValor ${valorBuscado} no encontrado.`);
  }
}

function main() {
  // 1. Declaracion y creacion de un arreglo de 10 enteros (10 posiciones en 0)
  const numeros = new Array(10).fill(0);

  // 2. Inicializacion con valores aleatorios (1 a 100)
  for (let i = 0; i < numeros.length; i++) {
    numeros[i] = Math.floor(Math.random() * 100) + 1;
  }

  // 3. Recorrido con for clasico (por indice)
  console.log("Arreglo (for clasico):");
  for (let i = 0; i < numeros.length; i++) {
    process.stdout.write(numeros[i] + " ");
  }

  // 4. Recorrido con for-each (for...of, por valor)
  console.log("\n\nArreglo (for-each):");
  for (const num of numeros) {
    process.stdout.write(num + " ");
  }

  // 5. Modificacion (a): impares a cero
  for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] % 2 !== 0) {
      numeros[i] = 0;
    }
  }
  console.log("\n\nDespues de cambiar impares por 0:");
  imprimir(numeros);

  // 5. Modificacion (b): multiplicar cada valor por su indice
  for (let i = 0; i < numeros.length; i++) {
    numeros[i] = numeros[i] * i;
  }
  console.log("\nDespues de multiplicar por el indice:");
  imprimir(numeros);

  // 6. Busqueda lineal
  buscar(numeros, 0);   // siempre esta: numeros[0] * 0 = 0
  buscar(numeros, 15);  // nunca esta: 15 es impar y habria quedado en 0
}

main();
