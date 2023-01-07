print("---"*15,"Tabela Pokémon", "---"*15)
class Pokemon:
    def __init__(self,nome,vida,ataque,defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa


    def exibir_descricao(self):
        print("=="*15,"INFORMAÇÕES TÉCNICAS","=="*15)
        descricao = (f"NOME: {self.nome} | VIDA:{self.vida} | ATQ:{self.ataque} | DEF:{self.defesa}|")
        print()
        return descricao 
        # metodo para mostrar a ficha ou descrição da class pokemon(padrão)


class tipo_pokemon(Pokemon):
    
    def __init__(self, nome,vida,ataque,defesa,tipo): # aplica um novo atributo para o pokemon2
        super().__init__(nome,vida,ataque,defesa) # Função super não usa self(O super já faz isso)
        self.tipo = tipo
        # função super para refereciar com a classe pokemon atráves do atributos dela própria

    def exibir_descricao(self): # criação de segundo metedo/ou ação com  o atributo mais na CLASSE TIPO_POKEMON
        print("=="*15,"INFORMAÇÕES TÉCNICAS","=="*15)
        descricao = (f"NOME: {self.nome} | VIDA:{self.vida} | ATQ:{self.ataque} | DEF:{self.defesa}| TIPO:{self.tipo}")
        print()
        return descricao
            

p1 = Pokemon("FireBird","5.000", "3.450","2.500")
p2 = tipo_pokemon("Dragão Boladão","6.500","4.500", "5.500", "Voador")
print(p1.exibir_descricao()) # exibe a descrição pro primeiro pokemon
print(p2.exibir_descricao())        

