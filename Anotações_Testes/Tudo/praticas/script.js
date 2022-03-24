var receberClick = document.getElementById("area");
receberClick.addEventListener("click", MouseClicar);
receberClick.addEventListener("mouseenter", MouseEntrar);
receberClick.addEventListener("mouseout", MouseSair)

function MouseClicar() {
    receberClick.innerText = "Você clicou! :)"
    receberClick.style.background = "green"
    receberClick.style.color = "#7FFF00"
}

function MouseEntrar() {
    receberClick.innerText = "Você entrou com o mouse! :O"
    receberClick.style.background = "black"
    receberClick.style.color = "white"
}

function MouseSair() {
    receberClick.innerText = "Você saiu com o mouse! :("
    receberClick.style.background = "blue"
    receberClick.style.color = "aqua"
}