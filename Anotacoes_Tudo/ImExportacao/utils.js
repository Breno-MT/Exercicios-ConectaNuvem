export const testeExport = 42;

export class Pessoa {
  constructor(nome, idade) {
    this.nome = nome;
    this.idade = idade;
  }
}

export function daOi() {
    console.log('Oi!');
}

export const oi = () => console.log('Oi denovo');

//Método pra deixar tudo em um lugar e só usar o . para chamar
export const utilitario = {
    daOi,
    testeExport,
    Pessoa,
}