class Cliente {
    constructor (cpf) {
        this.cpf = cpf;
    }

    validarCPF(cpf) {
        
        if (cpf.length == 11) {
            console.log("Seu CPF foi validado")
        } else if (cpf.length != 11 && cpf) {
            console.log("Seu CPF não é valido!")
        }

    }
}

var Teste = new Cliente(12345678910).validarCPF();
