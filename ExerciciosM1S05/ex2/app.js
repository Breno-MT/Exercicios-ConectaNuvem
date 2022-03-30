const arrayNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9];

let arrayQuadrados = arrayNumeros.map(numero => numero ** 2)

const filtrar = arrayQuadrados.filter(numero => {
    return numero > 30;
})

console.log(filtrar)