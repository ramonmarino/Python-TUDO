try:
    a = int(input("Digite por favor um número: "))
    b = int(input("Digite o segundo número por favor: "))
    r = a/b
except (ValueError,TypeError): 
    print(f"Erro nos tipos de dados inseridos :(") 

except(ZeroDivisionError):
    print("Não é possível dividir por zero.")

except(KeyboardInterrupt):
    print("O usuário preferiu não informar os dados.")

else:
    print(f"O resultado foi: {r:.1f}")
finally:
    print("Volte sempre!")    