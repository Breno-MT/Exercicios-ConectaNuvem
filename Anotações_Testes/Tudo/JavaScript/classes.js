//class Cachorro {
    //constructor (nome, raca){
       // this.nome = nome;
       // this.raca = raca;
   // }

    //latir() {
        //console.log(`O ${this.nome} da raça ${this.raca} ! Rauf rauf!`);
   // }
//}

//const rex = new Cachorro("Dimitri", "Rex");
//rex.latir();

//const salsicha = new Cachorro("Pequeno", "anão");
//salsicha.latir();


//class Quadrado {
    //constructor (lado){
        //this.lado = lado;
    //}
//}

//const quadrado = new Quadrado(4);
//console.log(quadrado)


//class Monstro {
    //constructor (vida, velocidade) {
        //this.vida = vida;
        //this.velocidade = velocidade;
    //}

    //ataque(){
        //return "O mostro vai atacar!"
    //}
//}

//const monstro1 = new Monstro(30,5);
//const monstroAtaque = new Monstro(30,5).ataque();

//console.log(monstro1);
//console.log(monstroAtaque);


// class Endereco {
//     constructor (logradouro, numero, cidade, estado, pais, cep) {
//         this.logradouro = logradouro;
//         this.numero = numero;
//     }

//     mostrar() {
//         console.log(`${this.logradouro}, número ${this.numero}!`)
//     }
// }

// const mostrarAAA = new Endereco("Rua B", 5).mostrar();

class Veiculo {
    constructor(tipoVeiculo, marca, modelo, ano, placa, numMultas, velocidadeMaxima) {
        this.tipoVeiculo = tipoVeiculo;
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.placa = placa;
        this.numMultas = numMultas;
        this.velocidadeMaxima =velocidadeMaxima;
    }

    getTipoModelo(){
        return `Carro tipo: ${this.tipoVeiculo}, modelo: ${this.modelo}`
    }
    adicionaMulta(placa){
        if(placa == this.placa){
            this.numMultas++
            console.log(`Número de multas ${this.numMultas}`);
        }
        else{
            console.log('Placa inválida');
        }

    }
}

const bmwX5 = new Veiculo('Esportivo','BMW','x5','2019','AAA-0000', 3,300); 
bmwX5.adicionaMulta('AAA-0000');
console.log(bmwX5.getTipoModelo()); 
bmwX5.adicionaMulta('AAA-000');