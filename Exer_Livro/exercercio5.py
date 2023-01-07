"""Escreva um programa que pergunte a velocidade de um carro do usuário
Caso ultrapasse 80 km/h. Exiba uma menssagem dizendo que o usuário foi multado
Nesse caso, Exiba o valor da multa. Cobrando R$ 5 por Km acima da velocidade."""

print("=-="*10,"PROGRAMA DE MULTAS","=-="*10)

velocidade = int(input("Digite a velocidade atual do carro: "))
if velocidade > 80:
    multa = (velocidade - 80)*5
    print("Você foi multado, por favor diminua a velocidade.")
    print(f"velocidade do carro estava: {velocidade} Km/h")
    print(f"Na via só permitido 80Km/h,valor da multa a pagar:R${multa}")

else: 
    print("Você pode seguir viagem!")
    print("Lembre-se de colocar o cinto!")    
