class Transacoes {
    constructor(conta, valorDaTransacao, numeroDaConta) {
      this.conta = conta;
      this.valorDaTransacao = valorDaTransacao;
      this.idDeTransferencia = 1;
      this.data = new Date();
      this.numeroDaConta = numeroDaConta;
    }
  
    get transferencia() {
      return this.fazerTransferencia();
    }
  
    fazerTransferencia() {
      return `Transferencia feita, novo saldo: ${(this.conta -= this.valorDaTransacao)}`;
    }
  
    get deposito() {
      return this.fazerDeposito();
    }
  
    fazerDeposito() {
      this.idDeTransferencia++;
      return `Deposito feito, novo saldo: ${(this.conta += this.valorDaTransacao)} ID da transação: ${
        this.idDeTransferencia
      } na data: ${this.data}`;
    }
  }