const p = document.getElementById('display');
const campoCEP = document.getElementById('campoCEP');
const btnCEP = document.getElementById('btn-cep');


function validaCEP(cep) {
    if (cep.length !== 7) {
        return false;
    } 
    return true;
}

async function buscaCEP() {

    try {
        const cep = campoCEP.value;
    
        if(validaCEP(cep)) {
            throw new Error('CEP não informado!');
        }
    
        const url = `https://viacep.com.br/ws/${cep}/json`
    
        const resposta = await fetch(url);
        
        const conteudo = await resposta.json();
    
        console.log(conteudo)
        display.innerHTML = conteudo.localidade;

    } catch (erro) {

        console.log(erro);
        console.log('!!! DENTRO DO CATCH !!!');
        console.log(erro)
    }
  
}
btnCEP.addEventListener('click', buscaCEP);