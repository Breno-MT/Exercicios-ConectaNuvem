class Passagens:
    
    def __init__(self, numero, origem, destino):
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.__assentos_livres = [x+1 for x in range(0,25)]
        self.__valor_passagem = 250.90


    @property
    def check_discount(self):
        if self.__assentos_livres <= 10:
            self.__valor_passagem * 10/100
        
        elif self.__assentos_livres >= 11 and self.__assentos_livres <= 15:
            self.__valor_passagem * 15/100
            
        elif self.__assentos_livres >= 16 and self.__assentos_livres <= 20:
            self.__valor_passagem * 15/100
        
        elif self.__assentos_livres >= 20:
            self.__valor_passagem = self.__valor_passagem
        
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
            assento_comprado = int(input("""
                Baseado nos assentos disponíveis, digite o número do seu assento!
                -> """))
        
        elif opcao == "n":
            print("Obrigado, espero que volte sempre!")
    
    





