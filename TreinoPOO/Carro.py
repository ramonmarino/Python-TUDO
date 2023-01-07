class MarcaInvalid(Exception):
    pass

class Carro:
    def __init__(self,marca,valor):
        self.set_marca(marca)
        self.set_valor(valor) 

    def set_marca(self,nova_marca):
        if type(nova_marca) != str:
            raise MarcaInvalid
        self.set_marca = nova_marca

    def set_valor(self,novo_valor):
        if type(novo_valor) != float:
            raise ValueError
        self.valor = novo_valor 

try:
    cliente = Carro("BMW", "350.000")
except MarcaInvalid:
    print("Necessário que o nome da marca seja em texto.")
except ValueError:
    print("É necessário que o valor seja um número.")
else:
    print("Parabéns pela compra!")    