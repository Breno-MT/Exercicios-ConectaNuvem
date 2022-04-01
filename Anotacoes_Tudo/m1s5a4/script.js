const listaCEPs = {
    '88034001': {
        logradoura: "Rua do SENAI SC"
    }
}


// EXEMPLO DE PROMISE
function buscaCEPpromise(cep){

    //Promise(resolve, reject) <- já é pré-definido, só passar os nomes que quer usar no lugar,
    // ou pode colocar resolve e reject mesmo, respeitando a ordem sempre.
    return new Promise((resolve, reject) => {
        const resultado = listaCEPs[cep];
        const erro = resultado 
        ? false 
        : 'CEP Inválido!'
    
        if (erro) {
            reject(erro)
        } else {
            resolve(resultado)
        }
    
    });
}

buscaCEPpromise('88034001')
 .then(resultado => {
      console.log(resultado);
})
 .catch(erro => {
     console.log(erro);
 })
 .finally(() => {
     console.log("Sempre exec no fim de tudo")
 });


// EXEMPLO DE FETCH

const p = document.getElementById('display');
const campoCEP = document.getElementById('campo-cep');
const btnCEP = document.getElementById('btn-cep');



// function buscaCEPfetch() {

//     const cep = campoCEP.value;

//     if(!cep) {
//         display.innerHTML = 'Informe um CEP!';
//         return;
//     }

//     fetch(`https://viacep.com.br/ws/${cep}/json`)
//       .then(resposta => {
//         resposta.json()
//           .then(conteudo => {
//             console.log(conteudo);
//             p.innerHTML = conteudo.logradouro;
//           })
//       })
//       .catch(erro => {
//         console.log(erro)
//       });
    
//     fetch('/Anotacoes_Tudo/m1s5a4/texto.txt')
//         .then(resposta => {
//             resposta.text().then(conteudo => {
//                 console.log(conteudo);
//             })
//         })
//         .catch(erro => {
//             console.log(erro)
//         })


// }

//btnCEP.addEventListener('click', buscaCEPfetch);

// ASYNC WAIT

// promise com atraso
// function delay(ms) {
//     return new Promise(resolve => {
//         setTimeout(() => resolve('blah'), ms);
//     })
// }

//   // uma arrow function assíncrona
// async function buscaCEP(){

//     //comando de espera
//     const resposta = await delay(1000);

//     //executa após conclusão de delay
//     console.log('Terminei de esperar! ' + resposta)
// }

// roda o exemplo
//buscaCEP();
// imprime primeiro no console
//console.log('Executei o console log');


// async wait com fetch

// async function buscaCEPawait() {

//     const cep = campoCEP.value;

//     if(!cep) {
//         display.innerHTML = 'Informe um CEP!';
//         return;
//     }

//     const url = `https://viacep.com.br/ws/${cep}/json`

//     const resposta = await fetch(url);
    
//     const conteudo = await resposta.json();

//     console.log(conteudo)
//     display.innerHTML = conteudo.localidade;
 
//       //.catch(erro => {
//         //console.log(erro)
//       //});
    
// }
// btnCEP.addEventListener('click', buscaCEPawait);


// EXEMPLO COM TRY CATCH

function validaCEP(cep) {
    if (cep.length !== 8) {
        return false;
    } 
    return true;
}


async function buscaCEPtry() {

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
btnCEP.addEventListener('click', buscaCEPtry);