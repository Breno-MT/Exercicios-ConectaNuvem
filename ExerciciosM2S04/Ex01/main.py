import conta_modulo as conta

conta_1 = conta.Conta('Breno', '001')

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
