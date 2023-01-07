class Cadastro:
    def __init__(self,nome,data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def get_nome(self):
        return self.nome,self.data_nascimento

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_data(self,nova_data):
        self.data_nascimento = nova_data    
          
class Pessoa:
    def __init__(self,cabelo, altura):
        self.cabelo = cabelo
        self.altura = altura

    def get_padrao(self):
        return self.cabelo,self.altura

    def set_atributo(self,novo_cabelo,nova_altura):
        self.cabelo = novo_cabelo
        self.altura = nova_altura







novo = str(input("Digite por favor um novo nome: "))
n = str(input("Digite uma nova data de nascimento: "))

cabelo_novo = input("Digite a nova cor: ")
altura_nova = float(input("Digite uma nova altura: "))



c1 = Cadastro("Ramon", "29/07/1995") # instância 
print(c1.get_nome())
c1.set_nome(novo) # modifica o valor do objeto atributo
c1.set_data(n)
print("Novo nome aplicado no Cadastro: ",c1.get_nome())
c2 = Pessoa("Cor do cabelo do Ramon é: Preto",  " E a altura é: 1,76")
print(c2.get_padrao())
c2.set_atributo(cabelo_novo,altura_nova)
print("Após as mudanças ficou assim: ", c2.get_padrao())


