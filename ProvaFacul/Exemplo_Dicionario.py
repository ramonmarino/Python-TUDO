Dic = {"Produto" : "Tigela","Cor" : "Azul", "Preço": 14} # cria dicionário/chave : valor
print(Dic["Cor"]) # exibe o valor da chave
print()

Cadastro = {} # cria dicionário vazio
Cadastro["Nome:"] = "Ramon" # adiciona elementos no dicionário.
Cadastro["Sobrenome:"] = "Marino"
Cadastro["Empresa:"] = "Rockstar"
print(Cadastro)

print()

Registro = {"Nome":{"Primeiro": "Ramon","Último nome": "Marino"}, # o Registro tem todas as informações
"Conhecimento": ["Atividade física","Python","Java"],"idade":27} # A chave nome tem primeiro e ultimo de chaves
print(Registro["Nome"]) # retorna tudo da chave Nome
print(Registro["Nome"]["Último nome"]) # Retorna o Ultimo valor da chave nome
print(Registro["Conhecimento"][-1]) # retorna o ultimo elemento da lista
Registro["Conhecimento"].append("Jogador de fifa") # adiciona valor a lista dentro do dicionario

print( Registro["Conhecimento"]) # retorna a lista toda