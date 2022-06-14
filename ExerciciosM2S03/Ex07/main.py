import json

dicionario_normal = {'primeiro_nome': 'Uncle', 'segundo_nome': ' Bob', 'idade': '50'}

dicionario_json = json.dumps(dicionario_normal)

print(dicionario_json)
