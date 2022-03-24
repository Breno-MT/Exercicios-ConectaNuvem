class Dev {
    constructor(nome, idade, linguagem) {
        this.nome = nome;
        this.idade = idade;
        this.linguagem = linguagem;
    }

    apresentacao() {
        console.log(`Sou dev, trabalho com ${this.linguagem}! Meu nome é ${this.nome} e
        tenho ${this.idade} anos!`)
    }
}

class FrontEndDev extends Dev{
    constructor(nome, idade, linguagem, framework) {
        super(nome, idade, linguagem)
        //this.nome = nome;
        //this.idade = idade;
        //this.linguagem = linguagem;
        this.framework = framework;
    } 

    apresentacao() {
        console.log(`Sou FrontEnd, trabalho com ${this.linguagem}! Meu nome é ${this.nome} e
        tenho ${this.idade} anos e trabalho com o framework ${this.framework}!`)
    }
}

class BackEndDev extends Dev{
    constructor(nome, idade, linguagem, bancoDeDados) {
        super(nome, idade, linguagem)
        //this.nome = nome;
        //this.idade = idade;
        //this.linguagem = linguagem;
        this.bancoDeDados = bancoDeDados;
    } 

    apresentacao() {
        console.log(`Sou BackEnd, trabalho com ${this.linguagem}! Meu nome é ${this.nome} e
        tenho ${this.idade} anos e trabalho com o ${this.bancoDeDados}!`)
    }
}

const dev1 = new Dev ("Brenin", 20, "Java");
dev1.apresentacao();

const frontend1 = new FrontEndDev ("Junin", 20, "JavaScript", "ReactJS");
frontend1.apresentacao();

const backend1 = new BackEndDev ("Jorgin", 20, "C#", "mySQL")
backend1.apresentacao();
