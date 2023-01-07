class Veiculo:
    def __init__(self,rodas,cor,marca,preco, blindado = False):
        self.rodas = rodas
        self.cor = cor
        self.marca = marca
        self.preco = preco
        self.blindagem = blindado

    def descricao_completa(self):
        txt = f"{self.rodas} {self.cor} {self.marca} {self.preco} {self.blindagem}"
        return txt


class car(Veiculo):
    def __init__( self,rodas, cor, marca,preco,blindado = False):
        super().__init__(rodas,cor,marca,preco,blindado = False)
        self.ar_condicionado = True


class Moto(Veiculo):
    def __init__( self,rodas, cor, marca,preco,blindado = False):
        super().__init__(rodas,cor,marca,preco,blindado = False)

    def empinar(self):
        return "Estou enpinando na casa da vizinha..."   


class Caminhao(Veiculo):
    def __init__(self,rodas,cor,marca,preco,blindado = False):
        super().__init__(rodas,cor,marca,preco,blindado= False)
        self.capacidade_garga = "capacidade"


class pessoa:
    def __init__( self,nome,idade,veiculo):
        self.nome = nome
        self. idade = idade
        self.automovel = veiculo

    def valor_automovel(self):
        msg = f"O carro da pessoa {self.nome} fica no valor de: R${self.automovel}"

carro = car(30,"Preto","BMW",350.000,blindado = True)
cliente = pessoa("Ramon",27,)          

      

