


class Carro:
    def __init__(self, marca, cor, valor, aro):
        self.marca = marca
        self.cor = cor
        self.valor = valor
        self.aro = aro

    def show_room(self):
        print("=="*10, "TABELA DE CARROS", "=="*10)
        descricao = (f"MARCA: {self.marca} | PINTURA: {self.cor} | PREÇO: {self.valor} | ARO: {self.aro}|")
        print()
        return descricao

    def Escolha_carro(self): 
        self.valor = str(input("Escolha seu carro: [1 -BMW / 2 -AUDI]: "))
        if self.valor == "1":
            return c1.valor
        elif self.valor == "2":
            return c2.
        else:
            return print("Ecolhe direito, VAI CHORAR?")

                    


        

        
     


class modelo_opcional(Carro):
    # com a função super só precisa instanciar a atributo adicional
    def __init__(self, marca, cor, valor, aro, modelo):
        super().__init__(marca, cor, valor, aro)
        self.modelo = modelo

    def show_room(self):
        descricao = (f"MARCA: {self.marca} | PINTURA: {self.cor} | PREÇO: {self.valor} | ARO: {self.aro}| MODELO: {self.modelo}")
        print()
        return descricao





print()


class Caminhao(Carro):
    def __init__(self, marca, cor, valor, eixos):
        self.marca = marca
        self.cor = cor
        self.valor = valor
        self.eixos = eixos

    def porte_grande(self):
        print("=="*10, "TABELA DE CAMINHÔES","=="*10)
        print()
        descricao = (
            f"MARCA: {self.marca} | PINTURA:{self.cor} | PREÇO: {self.valor} | EIXOS: {self.eixos} ")
        print()
        return descricao


                     

  

c1 = Carro("BMW", "VERMELHO", " R$ 350.000", "30")
c2 = modelo_opcional("AUDI", "BRANCO", "R$: 600.000", "30", "Blindado")
c3 = Caminhao("MERCEDES", "CREME", "581,978", "6")

print(c1.show_room())
print(c2.show_room())
print(c3.porte_grande())
print(c1.Escolha_carro())









