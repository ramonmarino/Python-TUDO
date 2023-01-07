from classes import CarinhoDeCompras,Produto

carrinho = CarinhoDeCompras()
p1 = Produto("Agasalho", 60)
p2 = Produto("controle de video game", 250)
p3 = Produto("Filé Mion", 90)

carrinho.inserir_produto(p2)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p3)

carrinho.lista_produtos()
print(carrinho.soma_total()) # quando for um return usar print