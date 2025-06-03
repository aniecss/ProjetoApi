from ProjetoApi.produto import Produto
from ProjetoApi.usuario import Usuario
from ProjetoApi.carrinho import Carrinho
from random import randint

# criar produto e o usuario
produto1 = Produto('001', 'Camisa Preta', 20, 50)
usuario1 = Usuario('001', 'Amanda Farias', 20, 2231133)

# criando carrinho com o ID do usuário correto
carrinho = Carrinho(randint(1000, 9999), usuario1._id)
Carrinho.carrinhos.append(carrinho)

# adicionar produto no carrinho
carrinho.adicionar_item(produto1, 2)
carrinho.listar_itens()

def main():
    Carrinho.salvar_carrinhos()

if __name__ == '__main__':
    main()
