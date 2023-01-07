'''Faça um programa que solicite o preço de uma mercadoria
e o percetual de desconto, Exiba o valor do desconto e o preço a pagar.'''

print("=="*10,"MÁQUINA DE DESCONTO","=="*10)

preco = float(input("Digite o preço da mercadoria por favor: "))
porcetagem = int(input("Digite o valor do desconto por favor: "))

valor_desconto = preco * (porcetagem/100) # valor com desconto
print(f"Valor da mercadoria era: R$ {preco} com o desconto ficou em:R$ {valor_desconto}")
print("Volte sempre!")
