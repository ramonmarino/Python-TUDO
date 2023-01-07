
class NameInvalid(Exception):
    pass

class ValueError(Exception):
    pass


class pessoa:
    def __init__(self,nome,idade):
        self.set_nome(nome) # vai verificar a o dado digitado e modificar
        self.set_idade = idade

    def set_nome(self,novo_nome):
        if type(novo_nome) != str:
            raise NameInvalid #cria seu próprio erro.
        self.nome = novo_nome    # atribui um novo atributo

    def set_idade(self,nova_idade):
        if type(nova_idade) != int:
            raise ValueError
        self.idade = nova_idade

try:
    usuário = pessoa("Ramon",27)

except NameInvalid:
    print("O nome deve ser em formato de texto.")
except ValueError:
    print("O dado deve ser um valor númerico.")
else:
    print("Cadastro feito com sucesso!")        

