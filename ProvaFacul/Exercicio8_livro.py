""" Escreva um programa que receba do usuário dia,hora,minutos e segundos
e exiba o resultado no terminar"""

print("=="*10,"CONVERSÃO DE UNIDADES","=="*10)

quantidade_dias = int(input("Digite a quantidade de dias em horas:  "))
hora = float(input("Digite a hora do dia: "))
minutos = float(input("Digite por favor os minutos: "))
segundos = float(input("Digite por favor os segundos: "))

novo_segundo = quantidade_dias + hora + minutos + segundos * 3600

print(f"O valor total em segundos é: {novo_segundo}")

