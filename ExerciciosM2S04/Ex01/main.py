class Conta:
    def __init__(self, nome_titular, numero):
        self.nome_titular = nome_titular
        self.numero = numero
        self.__saldo = 0
        self.__saldo_limite = 8000
    
    def depositar(self, valor):
        self.__saldo += valor


    # Este método especial irá printar a conta
    def __str__(self):
        return str(self.__dict__)


conta_1 = Conta('Breno', '001')
conta_1.depositar(1500)
print(conta_1)
