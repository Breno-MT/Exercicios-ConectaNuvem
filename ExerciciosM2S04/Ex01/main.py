class Conta:
    def __init__(self, nome_titular, numero):
        self.nome_titular = nome_titular
        self.numero = numero
        self.__saldo = 0
        self.__saldo_limite = 8000
    
    # Função de Deposito 
    def depositar(self, valor):
        self.__saldo += valor

    # Função de saque
    def saque(self, valor):

        # Verificações de negação
        if valor > self.__saldo:
            print("Saque Negado!!! Valor maior que o saldo!")
        
        elif valor > self.__saldo and valor > self.__saldo_limite:
            print("Saque Negado!!! Valor maior que o saldo e o saldo limite!")
        
        elif valor > self.__saldo_limite:
            print("Saque Negado!!! Valor maior que o limite de saldo!")
        
        # Verificações de validação
        elif valor <= self.__saldo and valor <= self.__saldo_limite:
            print(f"Saque Efetuado!!! No valor de R${valor:.2f}!")
            self.__saldo -= valor
        
        elif valor <= self.__saldo:
            print(f"Saque Efetuado!!! No valor de R${valor:.2f}!")
            self.__saldo -= valor
        

    # Função de transferência
    def transferir(self):

        print("---"* 12)
        valor = int(input("Qual o valor a ser transferido?: "))

        titular = str(input("Digite o nome do titular que irá receber a transferência: "))
        numero_titular = str(input("Digite o número do titular que irá receber a transferência: "))

        global conta_escolhida
        conta_escolhida = Conta(titular, numero_titular)


        # Verificações de negação
        if valor > self.__saldo:
            print("Transferência Negada!!! Valor maior que o saldo!")
            print("---"* 12)
        
        elif valor > self.__saldo and valor > self.__saldo_limite:
            print("Transferência Negada!!! Valor maior que o saldo e o saldo limite!")
            print("---"* 12)
        
        elif valor > self.__saldo_limite:
            print("Transferência Negada!!! Valor maior que o limite de saldo!")
            print("---"* 12)
        
        # Verificações de validação
        elif valor <= self.__saldo and valor <= self.__saldo_limite:
            print(f"Transferência Efetuada!!! No valor de R${valor:.2f}!")
            print("---"* 12)
            self.__saldo -= valor
            conta_escolhida.__saldo += valor
        
        elif valor <= self.__saldo:
            print(f"Transferência Efetuada!!! No valor de R${valor:.2f}!")
            print("---"* 12)
            self.__saldo -= valor
            conta_escolhida.__saldo += valor
        

    # Este método especial irá printar a conta
    def __str__(self):
        return str(f"Nome: {self.nome_titular}, N. Titular: {self.numero}, Saldo: R${self.__saldo:.2f}, Saldo Limite: R${self.__saldo_limite:.2f}")

conta_1 = Conta('Breno', '001')
conta_1.depositar(8001)
print(conta_1)
conta_1.transferir()
print(conta_1)
print("---"* 12)
print(conta_escolhida)
