// EXEMPLOS OPERADOR REST

// function apresenta(...resto) {
//     console.log(`Olá, ${resto}`)
// }

// apresenta('Breno', 20, "Programador", 'Junin')

// function somaTudo(a, ...numeros) {
//     console.log(a);
//     return numeros.reduce((acc, num) => acc + num, 0)
// }

// const result = somaTudo("Breno", 150, 1230, 234, 657, 7345, 4353, 213);
// console.log(result);

// EXEMPLOS DE SPREAD

// const pessoa = ['Breno', 29, 'Programador'];

// function apresenta(nome, idade, prof) {
//     console.log(`${nome}, ${idade}, (${prof})`)
// }

// apresenta(...pessoa);

// Obdece a ordem do spread
// const vetUm = [1,2,3,4];
// const vetDois = [5,6,7,8];
// const concat = [...vetDois, ...vetUm];

// console.log(concat);

// Nesse caso ele vai substituir pela ordem, por conta de ser Objeto
const objUm = {
    nome: 'Breno',
    idade: 20,
    prof: "Prog",
}
// const objDois = {...objUm};

// console.log(objDois)

// EXEMPLOS DESTRUCT

// renomeando um item de objeto
// pegando item com nome certo
// pegando restante dos itens
const { nome, idade, ...sobrou} = objUm;
console.log(nome, idade, sobrou);

const vet = [1,2,3,4,5];

const[a, b, ...blau] = vet;

console.log(a, b, blau);

function apresentaP({nome, idade, prof}) {

    console.log(`${nome}, ${idade}, ${prof}`)
}

apresentaP(objUm);

const complex = {
    //nomeEx: 'Juliana',
    itens: {key: 'chave'}
}

const {nomeEx = 'Breno', itens : {key} } = complex;
console.log(nomeEx, key)