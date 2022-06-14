def check_strings():

    carac_1 = str(input("Digite qualquer caracter especial: "))
    carac_2 = str(input("Digite qualquer caracter especial: "))
    nome_input = str(input("Digite alguma frase: "))

    # Checkagem caso o usuário não faça as seguintes coisas:

    carac_padrao = "-"
    nome_padrao = "Dev In House"

    if carac_1 == "" and carac_2 == "" and nome_input == "":
        print(f"{carac_padrao * 12} {nome_padrao:^} {carac_padrao * 12}")
    
    elif carac_1 != "" and carac_2 != "" and nome_input == "":
        print(f"{carac_1 * 12} {nome_padrao:^} {carac_2 * 12}")
    
    elif carac_1 != "" and nome_input != "" and carac_2 == "":
        print(f"{carac_1 * 12} {nome_input:^} {carac_padrao * 12}")

    elif carac_2 != "" and nome_input != "" and carac_1 == "":
        print(f"{carac_padrao * 12} {nome_input:^} {carac_2 * 12}")
    
    elif carac_1 == "" and carac_2 == "" and nome_input != "":
        print(f"{carac_padrao * 12} {nome_input:^} {carac_padrao * 12}")

    else:
        print(f"{carac_1 * 12} {nome_input:^} {carac_2 * 12}")

check_strings()
