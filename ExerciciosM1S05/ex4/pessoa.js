export class Pessoa {
    #PrivCPF
    constructor(nome, cpf) {
        this.nome = nome;
        this.#PrivCPF = cpf;
    }

    set #cpf(cpf) {
        this.#PrivCPF = cpf;
    }
    
    get #cpf(){
        return this.#PrivCPF;
    }

    imprime() {
        console.log(`Nome: "${this.nome}" e o seu CPF: "${this.#PrivCPF}"`)
    }
}