class Pessoa {
    ser(){
        console.log("Eu sou uma pessoa.")
    }
}

class Jovem extends Pessoa {

}

class Idoso extends Pessoa {
    ser() {
        console.log("Eu sou um idoso, pois tenho idade avançada!")
    }
}

const pessoa1 = [new Pessoa(), new Jovem()]
pessoa1.forEach(p1 => p1.ser());

const pessoa2 = new Idoso;
pessoa2.ser();