"""Escreva um programa que pergunte o salário do funcionário e calcule
 o valor do aumento, para salários superiores 1250,00,calcule um aumento de
 10% para os inferiores ou iguais de 15%"""

print("=="*10,"PROGRAMA DE CALCULO DE AUMENTO DE SALÁRIO","=="*10)

salario = float(input("Digite por favor o salário atual: "))
aumento = int(input("Digite a porcetagem de aumento que deseja: "))

if salario >= 1250.00:
    novo_salario = (salario + (salario*aumento/100))
    print(f" O novo salário como aumento é: R$ {novo_salario:.2f}")
elif salario < 1250.00:
    novo_salario =(salario + (salario*aumento/100))
    print(f"O novo salário com o aumento é: R$ {novo_salario:.2f}")
elif salario < 500:
      novo_salario =(salario + (salario*aumento/100))
      print(f"O novo salário com o aumento é: R$ {novo_salario:.2f}")

    