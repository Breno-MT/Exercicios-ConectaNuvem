const p1 = document.getElementById('p');
const input = document.getElementById('inputNome');
const botao = document.getElementById('btn');

botao.addEventListener("click", () => {
    mensagemOla(input)
})

const mensagemOla = input => {
    if(input.value) {
        return p1.innerHTML = "Olá, " + input.value + " !"
    } else {
        return p1.innerHTML = "Olá sem nome!"
    }
}