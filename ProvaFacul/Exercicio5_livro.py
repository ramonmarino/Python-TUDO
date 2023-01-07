"Modefique o programa 2.2 para um aumento de 15% e um salário de 750"

salario_atual = float(input("Digite o seu sálario mensal por favor: "))
aumento_salarial = float(input("Digite o aumento necessário: ")) 

novo_salário = salario_atual + salario_atual * (aumento_salarial/ 100) 

print(f"O novo salário é: {novo_salário:.2f}")