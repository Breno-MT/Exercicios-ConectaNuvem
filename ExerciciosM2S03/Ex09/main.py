class Passagens:
    
    def __init__(self, numero, origem, destino):
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.__assentos_livres = [x+1 for x in range(0,25)]
        self.__valor_passagem = 250.90
      
    @property
    def comprar_passagem(self):

        opcao = str(input(f""" Bem-vindo(a)! Obrigado por nos escolher!
            O valor da passagem integral é R${self.__valor_passagem:.2f} !
            Temos os seguintes assentos disponíveis:
            {self.__assentos_livres}

            Deseja comprar?
            S/N -> """))
        opcao.lower()
        if opcao == "s":

            global assento_comprado

            assento_comprado = int(input("""
                Baseado nos assentos disponíveis, digite o número do seu assento!
                -> """))
            
            if assento_comprado <= 10:
                assento_desconto = self.__valor_passagem * 25/100
                print(f"Obrigado pela preferencia! Seu número de voo é {passageiro.numero}, origem {passageiro.origem} com destino a {passageiro.destino}!")
                print(f"O valor da sua passagem com desconto é de 25%! Valor total: R${assento_desconto:.2f}")

            if assento_comprado >= 11 and assento_comprado <= 15:
                assento_desconto = self.__valor_passagem * 15/100
                print(f"Obrigado pela preferencia! Seu número de voo é {passageiro.numero}, origem {passageiro.origem} com destino a {passageiro.destino}!")
                print(f"O valor da sua passagem com desconto é de 15%! Valor total: R${assento_desconto:.2f}")

            if assento_comprado >= 16 and assento_comprado <= 20:
                assento_desconto = self.__valor_passagem * 5/100
                print(f"Obrigado pela preferencia! Seu número de voo é {passageiro.numero}, origem {passageiro.origem} com destino a {passageiro.destino}!")
                print(f"O valor da sua passagem com desconto é de 5%! Valor total: R${assento_desconto:.2f}")
            
            if assento_comprado >= 20:
                print(f"Obrigado pela preferencia! Seu número de voo é {passageiro.numero}, origem {passageiro.origem} com destino a {passageiro.destino}!")
                print(f"O valor da sua passagem não possui desconto! Valor total: R${self.__valor_passagem:.2f}")

            self.__assentos_livres.remove(assento_comprado)
            print(f"Assentos livres atualmente: {self.__assentos_livres}")
        
        elif opcao == "n":
            print("Obrigado, espero que volte sempre!")
    
    @property
    def alterarPoltrona(self):
        print(f"Os assentos disponíveis para troca são: {self.__assentos_livres} !")
        assento_alterado = int(input("Digite o número do assento desejado: "))

        self.__assentos_livres.append(assento_comprado)
        self.__assentos_livres.remove(assento_alterado)
        print(f"Assentos disponíveis atualmente são {self.__assentos_livres}")

    @property
    def cancelarPassagem(self):
        print(f"Você cancelou sua compra do assento {assento_comprado}! E o valor de R${self.__valor_passagem} foi retornado.")
        self.__assentos_livres.append(assento_comprado)
        print(f"Lista de passagem disponiveis: {self.__assentos_livres}")


        
passageiro = Passagens(1234, "Sao Paulo", "Florianópolis")
    
while True:
    print("-*-"*6)
    opcao = int(input(""" Bem-vindo(a) a nossa companharia aerea da Gol!
    [1] Comprar Passagem
    [2] Cancelar Passagem
    [3] Trocar Passagem
    [0] Sair

    Digite sua opção: """))

    if opcao == 1:
        opcao = passageiro.comprar_passagem
    
    elif opcao == 2:
        opcao = passageiro.cancelarPassagem

    elif opcao == 3:
        opcao = passageiro.alterarPoltrona

    elif opcao == 0:
        print("Até mais e volte sempre.")
        break

    else:
        print("Digite apenas uma das opções!")
