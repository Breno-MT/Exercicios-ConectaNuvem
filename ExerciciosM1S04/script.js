class Produto {
    constructor(){
        this.id = 1;
        this.arrayProdutos = [];
    }

    salvar() {
        let produto = this.lerDados();

        if (this.validaCampos(produto)) {
            this.adicionar(produto);
        }

        this.listaTabela();
        this.cancelar();
    }

    listaTabela() {
        let tbody = document.getElementById("tbody");

        tbody.innerText = '';

        
        for (let i = 0; i < this.arrayProdutos.length; i++) {    

            let tr = tbody.insertRow();
            let td_id = tr.insertCell();
            let td_produto = tr.insertCell();
            let td_valor = tr.insertCell();
            let td_acoes = tr.insertCell();

            
            
            td_id.innerText = this.arrayProdutos[i].id;
            td_produto.innerText = this.arrayProdutos[i].nomeProduto;
            td_valor.innerText = this.arrayProdutos[i].valorProduto;
            
            
            td_id.classList.add('center');
            td_acoes.classList.add('center');
            
            
            
            
            let imgEdit = document.createElement('img');
            imgEdit.src="./iconsHTML/editIcon.png";
            //imgEdit.setAttribute("onclick");
            td_acoes.appendChild(imgEdit);
            
            if (imgEdit && imgEdit.style){
                imgEdit.style.maxHeight = '25px';
                imgEdit.style.maxWidth= '25px';

            }
            
            
            let imgDelete = document.createElement('img');
            imgDelete.src="./iconsHTML/delete.jpg";
            imgDelete.setAttribute("onclick", "produto.deletar("+ this.arrayProdutos[i].id +")");
            td_acoes.appendChild(imgDelete);
            
            if (imgDelete && imgDelete.style){
                imgDelete.style.maxHeight = '25px';
                imgDelete.style.maxWidth= '25px';

            }
    
        }
    }

    adicionar(produto) {
        this.arrayProdutos.push(produto);
        this.id++;
    }

    cancelar() {
        document.getElementById("produto").value='';
        document.getElementById("valor").value='';
    }

    deletar(id) {
        let tbody = document.getElementById("tbody");

        if(confirm("Deseja excluir o id: " + id)){

            for (let i = 0; i < this.arrayProdutos.length; i++) {
    
                
                if(this.arrayProdutos[i].id == id) {
                    this.arrayProdutos.splice(i, 1)
                    tbody.deleteRow(i);
                }
            }
        }


    }

    editar(i) {

        // Não está completo.

        this.arrayProdutos[i] == i;

        this.arrayProdutos.splice(i, 1, nomeProduto, valorProduto)

        

    }


    lerDados() {
        let produto = {}

        produto.id = this.id;
        produto.nomeProduto = document.getElementById("produto").value;
        produto.valorProduto = document.getElementById("valor").value;

        console.log(produto)
        return produto;
    }

    validaCampos(produto) {
        let msg = '';

        if (produto.nomeProduto == '') {
            msg += 'Informe um nome de produto! ';
        }

        if (produto.valorProduto == '') {
            msg += 'Informe um valor para o produto! ';
        }

        if (msg != '') {
            alert(msg);
            return false;
        }

        return true;
    }
}

var produto = new Produto();