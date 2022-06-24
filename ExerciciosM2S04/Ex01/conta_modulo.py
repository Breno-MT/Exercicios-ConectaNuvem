class Conta:
    # Métodos de inicialização da Classe
    def __init__(self, nome_titular, numero):
        self.nome_titular = nome_titular
        self.numero = numero
        self.__saldo = 0
        self.__saldo_limite = 8000
    
    # Função de Deposito 
    def depositar(self):
        valor = float(input("Digite o valor a ser depositado R$: "))

        if valor <= 0:
            print("O valor deve ser acima de R$ 0.01 !")
        
        elif valor >= 0.01: 
            print(f"Depósito no valor de R${valor:.2f}! Efetuado com sucesso!!!")
            self.__saldo += valor

    # Função de saque
    def saque(self):

        valor = float(input("Digite o valor a ser sacado R$: "))

        # Verificações de negação
        if valor > self.__saldo:
            print("Saque Negado!!! Valor maior que o saldo! Consulte o seu banco!")
        
        elif valor > self.__saldo and valor > self.__saldo_limite:
            print("Saque Negado!!! Valor maior que o saldo e o saldo limite! Consulte o seu banco!")
        
        elif valor > self.__saldo_limite:
            print("Saque Negado!!! Valor maior que o limite de saldo! Consulte o seu banco!")
        
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
        valor = float(input("Qual o valor a ser transferido?: "))

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
            self.__saldo -= valor
            conta_escolhida.__saldo += valor
            print(conta_escolhida)
            print("---"* 12)
            
        
        elif valor <= self.__saldo:
            print(f"Transferência Efetuada!!! No valor de R${valor:.2f}!")
            self.__saldo -= valor
            conta_escolhida.__saldo += valor
            print(conta_escolhida)
            print("---"* 12)

    # Função de chamar o menu
    def main_menu():
        while True:
            opcao = int(input("""
            ___________________________________________________________________________
            |                           Olá! Bem-vindo(a) ao Conecta Banco!
            |
            |
            |
            |
            |
            |   [1] Saque
            |   [2] Depósito
            |   [3] Transferência
            |   [4] Extrato Bancário
            |   [0] Sair
            |    
            |
            |
            |   [->] """))
            
            if opcao == 1:
                opcao = conta_1.saque()

            elif opcao == 2:
                opcao = conta_1.depositar()

            elif opcao == 3:
                opcao = conta_1.transferir()

            elif opcao == 4:
                print(conta_1)

            elif opcao == 0:
                break

            else:
                print("Digite apenas uma das opções acima.")

    # Este método especial irá printar a conta
    def __str__(self):
        return str(f"Nome: {self.nome_titular}, N. Titular: {self.numero}, Saldo: R${self.__saldo:.2f}, Saldo Limite: R${self.__saldo_limite:.2f}")
