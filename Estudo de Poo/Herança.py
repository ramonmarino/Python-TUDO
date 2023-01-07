
class Pessoa:                    # Super Classe
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__ 

    def falar(self): # ação da classe,Método
        print(f"{self.nomeclasse} Estou conversando...")    


class Cliente(Pessoa): # Sub Classes
    def comprar(self):
        print(f"{self.nomeclasse} Estou comprando...") 



class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nomeclasse} Estou lendo... ")

class Familia(Pessoa):
    def limpar(self):
        print(f"{self.nomeclasse} Limpando a casa")
