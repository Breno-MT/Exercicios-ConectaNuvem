async function euNaoEspero() {
    aguarda3Segundos();
    console.log('Eu não espero')
}

// PODEMOS RESOLVER O PROBLEMA DA FUNÇÃO "euNaoEspero" COLOCANDO
// UM 'await' ANTES DA FUNÇÃO "aguarda3Segundos"
// EX: await aguarda3Segundos();
// IGUAL ESTÁ NA FUNÇÃO FEITA "euEspero" LINHA 18


async function aguarda3Segundos() {
    await new Promise(resolve => setTimeout(resolve, 3000)); // 3 sec
    console.log('Função diz: Terminei!');
}

async function euEspero() {
    await aguarda3Segundos();
    console.log('Esperei 3 segundos :D')
}

euNaoEspero();
euEspero();