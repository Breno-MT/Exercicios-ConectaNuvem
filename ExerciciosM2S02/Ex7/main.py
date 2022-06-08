import sys
from time import sleep
import matematica as mate

def main_menu():
    while True:

        sleep(1)
        print("Olá, as seguintes opções a seguir serão levadas em conta!")
        print("""Leve em conta as seguintes opções
            [1] Somar
            [2] Subtrair
            [3] Dividir
            [4] Multiplicação
            [5] Sair
        """)

        option = int(input("Digite uma opção -> "))
        

        if option == 1:
            num1 = int(input("Digite um número inteiro 1 -> "))
            num2 = int(input("Digite um número inteiro 2 -> "))
            print(mate.somar(num1, num2))

        elif option == 2:
            num1 = int(input("Digite um número inteiro 1 -> "))
            num2 = int(input("Digite um número inteiro 2 -> "))
            print(mate.subtrair(num1, num2))

        elif option == 3:
            num1 = int(input("Digite um número inteiro 1 -> "))
            num2 = int(input("Digite um número inteiro 2 -> "))
            print(mate.divisao(num1, num2))

        elif option == 4:
            num1 = int(input("Digite um número inteiro 1 -> "))
            num2 = int(input("Digite um número inteiro 2 -> "))
            print(mate.multiplicar(num1, num2))

        elif option == 5:
            print("Fim do programa.")
            sys.exit()

        else:
            print("Digite uma opção válida!")

main_menu()
