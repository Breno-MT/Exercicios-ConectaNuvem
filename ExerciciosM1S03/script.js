/* O loop deve ser no máximo até 10 Termos, nada mais do que isso, fazer apenas a raíz e o valor inicial.*/

function PA(){
    var valor = parseInt(document.getElementById("inicial").value);
    var razao = parseInt(document.getElementById("razao").value);
    var termo = parseInt(10)

    var pa = "";

    for(var count=1; count<= termo; count++){
        pa += "Termo "+count+" = "+valor+"<br />";
        valor += razao;

    }
    
    pa = document.getElementById('span').innerHTML = pa;
}