import requests
import os
import json
import simplejson

os.system("cls")

print("""

   ___                  _ _           ___ _  _ ___    _ 
  / __|___ _ _  ____  _| | |_ __ _   / __| \| | _ \_ | |
 | (__/ _ \ ' \(_-< || | |  _/ _` | | (__| .` |  _/ || |
  \___\___/_||_/__/\_,_|_|\__\__,_|  \___|_|\_|_|  \__/ 
                                                        
Desenvolvido by: Iboy-Exploitado utilizando a API da receita federal.

	""")
cnpj = input("Insira o CNPJ: ")
req = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}")

json = req.json()

for key, value in json.items():
    print(f'{key}:, {value}:') 

print("Desenvolvido by: Iboy-Exploitado")

