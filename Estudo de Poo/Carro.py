print("---"*10,"CATÁLOGO DE CARROS DE LUXO","---"*10)
class Carro:
    def __init__(self,modelo,cor,cavalos,valor):
        self.modelo = modelo # marca
        self.cor = cor
        self.cavalos = cavalos
        self.valor = valor


class BMW(Carro):    
    pass
      

  
c1 = BMW("bmw 10", "azul","400","250")
print(c1.modelo,c1.cor,c1.cavalos,c1.valor)





