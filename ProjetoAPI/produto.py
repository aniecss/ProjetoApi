import json

class Produto:
    produtos = []  # Lista dos produtos

    def __init__(self, id, nome, preco, estoque):
        self._id = id
        self._nome = nome
        self._preco = preco
        self._estoque = estoque

    def __str__(self):
        return f'{self._id} - {self._nome} - R${self._preco:.2f} - {self._estoque} unid.'

    @classmethod
    def criar_produto(cls):
        while True:
            id = input('Informe o ID do produto: ').strip()
            nome = input('Nome do produto: ').strip()

            try:
                preco = float(input('Preço: R$ '))
                estoque = int(input('Quantidade em estoque: '))
            except ValueError:
                print("Preço e estoque precisam ser numéricos.")
                continue

            novo_produto = cls(id, nome, preco, estoque)
            cls.produtos.append(novo_produto)

            print('Produto cadastrado com sucesso!')

            opcao = input('Deseja adicionar outro produto? [S/N]: ').strip().upper()
            if opcao != 'S':
                break

    @classmethod
    def listar_produtos(cls):
        if not cls.produtos:
            print("Nenhum produto cadastrado.")
            return

        print(f'{"ID":<5} | {"Produto":<20} | {"Preço":<10} | {"Estoque"}')
        print('-'*50)
        for p in cls.produtos:
            print(f'{p._id:<5} | {p._nome:<20} | R${p._preco:<10.2f} | {p._estoque}')

    def to_dict(self):
        return {
            'id': self._id,
            'nome': self._nome,
            'preco': self._preco,
            'estoque': self._estoque,
        }

    @classmethod
    def salvar_produtos(cls):
        dados = [p.to_dict() for p in cls.produtos]
        with open('produtos.json', 'w') as file:
            json.dump(dados, file, indent=4)
        print('Produtos salvos com sucesso!')

    @classmethod
    def carregar_produtos(cls):
        try:
            with open('produtos.json', 'r') as file:
                dados = json.load(file)
                cls.produtos = [cls(d['id'], d['nome'], d['preco'], d['estoque']) for d in dados]
            print('Produtos carregados com sucesso!')
        except FileNotFoundError:
            print("Arquivo 'produtos.json' não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
