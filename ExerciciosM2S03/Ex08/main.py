import json

dicionario_normal = {   'primeiro_nome': 'Uncle', 
                        'segundo_nome': ' Bob', 
                        'idade': '50'   }

dicionario_json = json.dumps(dicionario_normal)

print(dicionario_json)

dicionario_nome = str(input("Digite o nome: "))
dicionario_sobrenome = str(input("Digite o sobrenome: "))
dicionario_idade = int(input("Digite a idade: "))

dicionario_user = {   "primeiro_nome": dicionario_nome, 
                                        "segundo_nome": dicionario_sobrenome, 
                                        "idade": dicionario_idade   }

dicionario_user_json = json.dumps(dicionario_user)

print(dicionario_user_json)
