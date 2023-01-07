"""Escreva um programa para calcular a redução do tempo de vida
de um fumante, Pergunte a quantidade de cigarros fumados por dia e quantos
anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada 
cigarro, e calcule quantos dias de vida o fumante perderá.Exiba o total de dias."""

quant_cigarro = int(input("Quantos cigarros você fuma por dia? "))
quant_anos = int(input("Por quantos anos você já fuma: "))

quantidade_dias = quant_anos *365
total_cigarros = quantidade_dias * quant_cigarro

minutos = total_cigarros *10
dias_perdidos = float(minutos/1440)

print(f"Você perdeu o tempo estimado de vida: {dias_perdidos:.2f} dias.")