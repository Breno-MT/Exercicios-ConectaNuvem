
// // arrow function
// function comum() {
//   console.log('comum');
// }

// const anonima = function () {
//   console.log('anonima')
// }

// // arrow function é anonima

// const arrow = () => {
//   console.log('arrow')
// }

// const arrowA = a => {
//   return `Olá, ${a}`
// }

// console.log(arrowA('Brenin'));


// function mostraThisA() {
//   console.log(this, this.nome);
// }

// const mostraThisB = () => {
//   console.log(this, this.nome);
// }

// const fruta = {
//   nome: "Melão",
//   imprimirA : mostraThisA,
//   imprimirB : mostraThisB
// };

// // anonima();
// // comum();
// // arrow();

// // fruta.imprimirA();
// // fruta.imprimirB();


// revisão de métodos de arrays

const vet = [1,2,3,4,5,6,7,8,9];

// vet.forEach(function (numero) {
//   console.log(numero);
// })

// vet.forEach(numero => console.log(numero))

// const result = vet.map(numero => numero * 4)

// console.log(result);


// const result = vet.filter(item => {
//   return item > 5;
// })

// console.log(result)

// const result = vet.every(item => {
//   return item > 0;
// })

// console.log(result)

// const result = vet.some(item => {
//   return item === 3;
// })

// console.log(result);

// let acumulador = 0;

// const result = vet.forEach(item => acumulador += item);

// console.log(acumulador);

// const result = vet.reduce((acc, item) => {
//   return acc += item
// }, 0);

// acc = acumulador
// const result = vet.reduce((acc,item) => acc + item, 0);

// console.log(result)

// const produtos = [
//   {nome: 'batata', qtd: 2, preco: 4},
//   {nome: 'arroz', qtd: 3, preco: 3}
// ]

// const total = produtos.reduce((acc, item) => acc + (item.qtd * item.preco), 0);

// console.log(total)