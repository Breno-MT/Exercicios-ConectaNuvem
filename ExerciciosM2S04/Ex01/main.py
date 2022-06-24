class Conta:
    def __init__(self, nome_titular, numero):
        self.nome_titular = nome_titular
        self.numero = numero
        self.__saldo = 150
        self.__saldo_limite = 8000
    

    def __str__(self):
        return str(self.__dict__)

conta_1 = Conta('Breno', '001')

print(conta_1)
