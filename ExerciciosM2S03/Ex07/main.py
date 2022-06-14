import json

dicionario = {'primeiro_nome': 'Uncle', 'segundo_nome': ' Bob', 'idade': '50'}

dicionario_json = json.dumps(dicionario)

print(dicionario_json)
