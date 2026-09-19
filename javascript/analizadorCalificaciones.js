const readline = require("readline");

// Se crea el iterador de lineas de inmediato para no perder lineas
// cuando la entrada llega por redireccion (por ejemplo: node archivo.js < datos.txt).
const rl = readline.createInterface({ input: process.stdin });
const lineas = rl[Symbol.asyncIterator]();

/** Muestra el mensaje y espera una linea de texto del usuario. */
async function preguntar(mensaje) {
  process.stdout.write(mensaje);
  const { value, done } = await lineas.next();
  if (done) {
    throw new Error("\nSe termino la entrada antes de completar los datos.");
  }
  return value.trim();
}

/** Lee un entero; si el usuario escribe otra cosa, lo vuelve a pedir. */
async function leerEntero(mensaje) {
  while (true) {
    const texto = await preguntar(mensaje);
    if (/^[+-]?\d+$/.test(texto)) {
      return Number(texto);
    }
    mensaje = "Entrada invalida. Ingrese un numero entero: ";
  }
}

/** Lee un decimal; si el usuario escribe otra cosa, lo vuelve a pedir. */
async function leerDecimal(mensaje) {
  while (true) {
    const texto = await preguntar(mensaje);
    if (texto !== "" && Number.isFinite(Number(texto))) {
      return Number(texto);
    }
    mensaje = "Entrada invalida. Ingrese un numero: ";
  }
}

async function main() {
  const n = await leerEntero("Ingrese el numero de calificaciones (N): ");

  if (n <= 0) {
    console.log("El numero de calificaciones debe ser mayor a 0.");
    return;
  }

  const calificaciones = new Array(n).fill(0);
  let aprobados = 0;
  let reprobados = 0;
  let suma = 0;

  // Lectura y validacion (0 - 100)
  for (let i = 0; i < n; i++) {
    while (true) {
      const cal = await leerDecimal(`Ingrese la calificacion ${i + 1} (0-100): `);
      if (cal >= 0 && cal <= 100) {
        calificaciones[i] = cal;
        suma += cal;
        if (cal >= 60) { // Criterio: Aprobado >= 60
          aprobados++;
        } else {
          reprobados++;
        }
        break;
      } else {
        console.log("Error. Ingrese entre 0 y 100.");
      }
    }
  }

  // Calculo del promedio
  const promedio = suma / n;

  console.log("\n--- RESULTADOS ESTADISTICOS ---");
  console.log(`Promedio: ${promedio.toFixed(2)}`);
  console.log(`Aprobados: ${aprobados} (${(aprobados / n * 100).toFixed(1)}%)`);
  console.log(`Reprobados: ${reprobados} (${(reprobados / n * 100).toFixed(1)}%)`);
}

main()
  .catch((error) => {
    console.error(error.message);
    process.exitCode = 1;
  })
  .finally(() => rl.close());
