string1 = str(input("Digite o primeiro string: "))
string2 = str(input("Digite o segundo string: "))

string_total = string1 + string2

# verifica se as string1 e string2 estão na soma total
def check_in():
    
    if string1 and string2 in string_total:
        print(f"As palavras3 {string1} e {string2} está na palavra {string_total} !")
    
    if string1 and string2 not in string_total:
        print("Por algum motivo, as strings não estão na palavra final!")

print(f"""
    A primeira string tem o tamanho de: {len(string1)}
    A segunda string tem o tamanho de: {len(string2)}
    As duas strings juntas formam: {string_total}

    O primeiro valor repetido 3 vezes!
    [-] {string1 * 3}
""")
check_in()
