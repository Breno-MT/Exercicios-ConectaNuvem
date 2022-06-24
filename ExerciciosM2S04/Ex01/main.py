class Conta:
    def __init__(self, nome_titular, numero):
        self.nome_titular = nome_titular
        self.numero = numero
        self.__saldo = 0
        self.__saldo_limite = 8000
    
    def depositar(self, valor):
        self.__saldo += valor


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
        

    # Este método especial irá printar a conta
    def __str__(self):
        return str(self.__dict__)


conta_1 = Conta('Breno', '001')
conta_1.depositar(8001)
conta_1.saque(8000)
print(conta_1)
