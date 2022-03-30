export class Pessoa {
    #_cpf
    constructor(nome, cpf) {
        this.nome = nome;
        this.#_cpf = cpf;
    }

    set #cpf(cpf) {
        this.#_cpf = cpf;
    }
    
    get #cpf(){
        return this.#_cpf;
    }

    imprime() {
        console.log(`Nome: "${this.nome}" e o seu CPF: "${this.#cpf}"`)
    }
}