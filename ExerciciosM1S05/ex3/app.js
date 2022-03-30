var nome = document.getElementById('campoProduto');
var p1 = document.getElementById('exibir');
var p2 = document.getElementById('total')
var btn = document.getElementById('btn');


const produtosArray = [
    {nome:'arroz', preco:9},
    {nome:'feijao', preco:12},
    {nome:'batata', preco:8},
    {nome:'macarrao', preco:5}
]


const totalValor = produtosArray.reduce((acc, item) => acc + item.preco, 0);
p2.innerHTML = `Valor total dos preços dos Produtos R$${totalValor}`;

btn.addEventListener("click", () => {
    var item = procura(nome.value, produtosArray)

    if(item){
        p1.innerHTML = `Produto: ${item.nome} e o seu Preço é R$: ${item.preco}`
    }else{
        p1.innerHTML = `Produto não encontrado.`
    }
})


function procura(nome, lista){
    var item = lista.find(n => n.nome === nome)
    return item
}