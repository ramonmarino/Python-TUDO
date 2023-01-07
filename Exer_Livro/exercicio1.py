"""Escreva um programa que calcule o tempo de uma viagem
de carro, pergunte a distância e a velocidade média esperada para a viagem"""

print("=-="*10,"PROGRAMA DE ESTIMATIVA DE TEMPO","=-="*10)

distancia = float(input("Digite por favor a distância da viagem em Km: "))
vel = int(input("Digite a velocidade média do carro: "))

tempo = distancia/vel

print(f"O tempo estimado da viagem em horas é:{tempo:.2f}h")