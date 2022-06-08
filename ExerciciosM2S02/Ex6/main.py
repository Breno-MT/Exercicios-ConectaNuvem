import sys
from time import sleep


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
            print(somar(num1, num2))

        elif option == 2:
            num1 = int(input("Digite um número inteiro 1 -> "))
            num2 = int(input("Digite um número inteiro 2 -> "))
            print(subtrair(num1, num2))

        elif option == 3:
            num1 = int(input("Digite um número inteiro 1 -> "))
            num2 = int(input("Digite um número inteiro 2 -> "))
            print(divisao(num1, num2))

        elif option == 4:
            num1 = int(input("Digite um número inteiro 1 -> "))
            num2 = int(input("Digite um número inteiro 2 -> "))
            print(multiplicar(num1, num2))

        elif option == 5:
            print("Fim do programa.")
            sys.exit()

        else:
            print("Digite uma opção válida!")

def somar(a,b):
    print("-*-"*6)
    return a + b

def multiplicar(a,b):
    print("-*-"*6)
    return a * b

def subtrair(a,b):

    print("-*-"*6)
    return a - b

def divisao(a,b):
    print("-*-"*6)
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Não tente dividir por 0! {e}")
    except:
        print("Tente novamente.")
    print("-*-"*6)




main_menu()