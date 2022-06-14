import json

dicionario_normal = {   'primeiro_nome': 'Uncle', 
                        'segundo_nome': ' Bob', 
                        'idade': '50'   }

dicionario_json = json.dumps(dicionario_normal)

print(dicionario_json)

nome_dict = str(input("Digite o nome: "))
sobrenome_dict = str(input("Digite o sobrenome: "))
idade_dict = int(input("Digite a idade: "))

dict_user = {   "primeiro_nome": nome_dict, 
                "segundo_nome": sobrenome_dict, 
                "idade": idade_dict   }

dict_user_json = json.dumps(dict_user)

print(dict_user_json)
