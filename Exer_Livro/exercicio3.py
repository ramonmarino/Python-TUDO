"""Escreva um programa que pergunte a quantidade de Km
perccorida por um carro alugado pelo usuário, e a quantidade de dias
que o carro foi alugado. calcule o preço a pagar, sabendo que o carro custa
 R$ 60 por dia e 0,15 km rodado"""

km = float(input("Digite por favor quantos km serão rodados: "))
dias = int(input("Quantos dias ficará com o carro: "))

preco = (dias * 60) + (km*0.15) # calculo para alguel de carro.

print(f"O preço do carro alugado ficou: R$:{preco:.2f}")