function validar() {
    var usuario = document.getElementById("usuario").value;
    var password = document.getElementById("senha").value;

    if(usuario == "aluno" && password == "senha123") {

        alert("Login foi realizado com sucesso!")
    }
    else{
        alert("Preencha os campos corretamente!")
    }

}