"""Faça um programa que calcule um aumento de salário
ele deve solicitar o valor do salário e a porcetagem do aumento
exiba valor do aumento e da porcetagem"""

print("--"*10,"BONÛS DE SALÁRIO","--"*10)

salario_atual = float(input("Digite por favor o salário: "))
porcetagem_valor =float(input("Digite por favor o valor do aumento: "))

novo_salario = salario_atual + salario_atual * (porcetagem_valor / 100)

print(f"O valor do salário era: R$ {salario_atual}")
print(f"O bonûs em cima do salário foi de:  {porcetagem_valor:.0f}%")
print(f" O salário com aumento ficou no valor corrigido de: R$ {novo_salario:.2f} ")