string1 = str(input("Digite o primeiro string: "))
string2 = str(input("Digite o segundo string: "))

string_total = string1 + string2

def check_in():
    
    if string1 and string2 in string_total:
        print(f"As palavra {string1} e {string2} está na palavra {string_total} ")



print(f"""
    A primeira string tem o tamanho de: {len(string1)}
    A segunda string tem o tamanho de: {len(string2)}
    As duas strings juntas formam: {string_total}
""")
check_in()

