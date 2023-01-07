print("---"*10, "Lista de Pokemon", "---"*10)  # classe mãe e global
print()


class Pokemon:
    def __init__(self, nome, vida, ataque, defesa, tipo, fraqueza):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.tipo = tipo
        self.fraqueza = fraqueza
    # Criação dos Métodos do Pokemon (açôes)

    def Centauro(self):
        print("Velocidade: Desconhecida.")
        print("Alimentação: Carnívoro ou Herbívoro.")
        print("Nível raridade: Super raro.")
        print("Ataque principal: Arco do Triunfo.")
        print("Comportamento: Amistoso.")

    def Bull(self):
        print("corre a 100 km")
        print("Se alimenta de grama das regiões altas...")
        print("Nível de raridade: Comum.")
        print("Ataque principal: Investida Mortal.")
        print("Comportamento: Arisco.")

    def Dragonspeed(self):
        print("Consegue voar longas distâncias.")
        print("Se alimenta de insetos... ")
        print("Nível de raridade: Raro.")
        print("Ataque principal: Desconhecido..")
        print("Comportamento: Desconhecido.")

    def WaterFish(self):
        print("Localizado nos mares do norte Meridian")
        print("Se alimenta de Peixes. ")
        print("Nível de raridade: Lendário.")
        print("Ataque principal: Tornado dos sete mares.")
        print("Comportamento: Agressivo.")


class Cavalo(Pokemon):  # escopo local
    def __init__(self, nome, vida, ataque, defesa, tipo, fraqueza):  # atributo adicional
        self.tipo = tipo  # o atributo.
        self.fraqueza = fraqueza
        super().__init__(nome, vida, ataque, defesa, tipo, fraqueza)  # polimorfirmo


class Alado(Pokemon):
    def __init__(self, nome, vida, ataque, defesa, tipo, fraqueza, montaria):
        self.tipo = tipo
        self.montaria = montaria
        self.fraqueza = fraqueza
        super().__init__(nome, vida, ataque, defesa, tipo, fraqueza)


class Aquático(Pokemon):
    def __init__(self, nome, vida, ataque, defesa, tipo, fraqueza, navegar):
        self.tipo = tipo
        self.navegar = navegar
        self.fraquza = fraqueza
        super().__init__(nome, vida, ataque, defesa, tipo,
                         fraqueza)  # faz referência a classe mãe


p1 = Cavalo("Centauro|", "3000 HP|", "400 ATQ|",
            "700 DEF|", "TIPO: Fogo", "FRA: Água |")
print(p1.nome, p1.vida, p1.ataque, p1.defesa, p1.tipo, p1.fraqueza)
print("---"*5, "FICHA TÉCNICA", "---"*5)
p1.Centauro()
print("___"*17)
p2 = Pokemon("Bull |", "8000 HP |", "900 ATQ |",
             " 1400 DEF |", "TIPO: Terra", "FRA: Gelo |")
print(p2.nome, p2.vida, p2.ataque, p2.defesa, p2.tipo, p2.fraqueza)
print("---"*5, "FICHA TÉCNICA", "---"*5)
p2.Bull()
print("___"*25)
p3 = Alado("DragonSpeed |", "10.000 HP |", "1000 ATQ |",
           "2000 DEF |", "TIPO: Voador |", "FRA: Fogo |", "Pode Montar| ")
print(p3.nome, p3.vida, p3.ataque, p3.defesa,
      p3.tipo, p3.fraqueza, p3.montaria)
print("---"*5, "FICHA TÉCNICA", "---"*5)
p3.Dragonspeed()
print("___"*25)
p4 = Aquático("WaterFish|", "4000 HP |", " 1450 ATQ |",
              "2500 DEF |", "TIPO: Água |", "FRA: Terra |", "Pode Navegar|")
print(p4.nome, p4.vida, p4.ataque, p4.defesa, p4.tipo, p4.fraqueza, p4.navegar)
print("---"*5, "FICHA TÉCNICA", "---"*5)
p4.WaterFish()
print("___"*25)
