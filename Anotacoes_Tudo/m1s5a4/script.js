const listaCEPs = {
    '88034001': {
        logradoura: "Rua do SENAI SC"
    }
}

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
     console.log("Fim :D")
 });