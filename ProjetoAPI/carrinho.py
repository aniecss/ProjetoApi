import json

class Carrinho:
    carrinhos = []

    def __init__(self, id, id_usuario, status="aberto"):
        self._id = id
        self._id_usuario = id_usuario
        self._status = status
        self._itens = []  # Lista de produtos no carrinho

    def __str__(self):
        return f'{self._id} - Usuário: {self._id_usuario} - Status: {self._status}'

    def adicionar_item(self, produto, quantidade):
        self._itens.append({
            'id': produto._id,
            'nome': produto._nome,
            'preco': produto._preco,
            'quantidade': quantidade
        })
        print(f"Produto '{produto._nome}' adicionado ao carrinho!")

    def listar_itens(self):
        print(f'Carrinho do usuário {self._id_usuario}:')
        for item in self._itens:
            print(f"- {item['nome']} | R${item['preco']} x {item['quantidade']}")

    def to_dict(self):
        return {
            'id': self._id,
            'id_usuario': self._id_usuario,
            'status': self._status,
            'itens': self._itens
        }

    @classmethod
    def salvar_carrinhos(cls):
        dados = [c.to_dict() for c in cls.carrinhos]
        with open('carrinhos.json', 'w') as f:
            json.dump(dados, f, indent=4)
        print("💾 Carrinhos salvos com sucesso!")

    @classmethod
    def carregar_carrinhos(cls):
        try:
            with open('carrinhos.json', 'r') as f:
                dados = json.load(f)
                cls.carrinhos = []
                for d in dados:
                    carrinho = cls(d['id'], d['id_usuario'], d['status'])
                    carrinho._itens = d['itens']
                    cls.carrinhos.append(carrinho)
            print("Carrinhos carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo 'carrinhos.json' não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
