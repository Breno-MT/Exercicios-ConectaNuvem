class Produto {
    constructor(produtos, nome, qtd, valor) {
        this.nome = nome;
        this.qtd = qtd;
        this.valor = valor;

    }



    calculaTotal(){

    }

}

const arroz = new Produto('arroz', 3, 9);
const feijao = new Produto('feijao', 2, 12);
const batata = new Produto('batata', 4, 8);
const macarrao = new Produto('macarrao', 1, 5);
const total = calculaTotal(arroz, feijao, batata, macarrao);
console.log(total);