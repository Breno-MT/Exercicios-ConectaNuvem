export default class Produto{
    #_nome 
    #_quantidade 
    #_valor 
    constructor(nome, qtd, valor){
        this.#nome = nome 
        this.#quantidade = qtd
        this.#valor = valor
    }
    set #nome(nome){
        this.#_nome = nome
    }
    get #nome(){
        return this.#_nome
    }
    set #quantidade(qtd){
        this.#_quantidade = qtd
    }
    get quantidade(){
        return this.#_quantidade
    }
    set #valor(valor){
        this.#_valor = valor
    }
    get valor(){
        return this.#_valor
    }

    
}