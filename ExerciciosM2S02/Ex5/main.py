import sys
from time import sleep


def main_menu():
    while True:

        sleep(1)
        print("""
            Olá, digite uma letra abaixo e descubra se é vogal ou consoante!

            [1] Descobrir a letra
            [2] Sair

        """)
        print('-*-'*6)
        opcao = int(input('Digite sua opção #> '))

        if opcao == 1:
            vogal_consoante()
        if opcao == 2:
            print("Até a próxima! :D")
            sys.exit()
        


vogal = ['a','e','i','o','u']
consoante = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

def vogal_consoante():

    print("-*-"*6)
    a = str(input("Digite sua letra!: "))

    if len(a) > 1:
        print("Digite apenas uma letra!")
        print('-*-'*6)
    if len(a) < 1:
        print("Digite uma letra!")
        print('-*-'*6)
      
    if a in vogal:
        print(f'Sua letra -> {a} <-  é uma vogal!')
        print('-*-'*6)
    if a in consoante:
        print(f'Sua letra -> {a} <- é uma consoante!')
        print('-*-'*6)

main_menu()