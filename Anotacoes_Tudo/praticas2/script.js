function calcular() {
    var tn1 = window.document.getElementById("txtnum1");
    var tn2 = window.document.getElementById("txtnum2");

    var operacao = window.document.getElementById("operacao");
    var resultado = window.document.getElementById("resultado");

    var n1 = Number(tn1.value);
    var n2 = Number(tn2.value);

    var operador = operacao.value;

    if (operador == "adicao") {
        var result = n1 + n2;
    }

    if (operador == "subtracao") {
        var result = n1 - n2;
    }

    if (operador == "multiplicacao") {
        var result = n1 * n2;
    }

    if (operador == "divisao") {
        var result = n1 / n2;
    }

    resultado.innerHTML = `A ${operador} entre ${n1} e ${n2} é: ${result}`;
}