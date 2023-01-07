try:
    idade = int(input("Digite sua idade: "))
    if not  (idade >= 26 and idade <=75):
        raise ValueError 

except ValueError:
    print("valor inválido: informe uma idade entre 26 e 75 anos.")
except TypeError:
    print("erro")
except:
    print("erro")            