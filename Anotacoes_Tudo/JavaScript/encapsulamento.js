class Pessoa {
    #nome
    #idade

    constructor (nome, idade){
        this.#nome = nome;
        this.#idade = idade;
    }

    get #nome() {
        return this.#nome;
    }
    
    set #nome(nome){ 
        this.#nome = nome;
    }

    exibir(){
        return `O meu nome é ${this.#nome} ! Tenho ${this.#idade} anos!`
    }
}

const p1 = new Pessoa("Brenin", 20);
console.log(p1.nome)

p1.nome = "Junin";
console.log(p1.nome)