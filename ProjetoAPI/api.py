from ProjetoApi.usuario import Usuario
from ProjetoApi.produto import Produto
from ProjetoApi.carrinho import Carrinho
from fastapi import FastAPI, HTTPException
from random import randint

app = FastAPI()

usuarios = {}
produtos = {}
carrinhos = {}

@app.post('/usuario')
def criar_usuario(nome: str, idade: int, cpf: int):
    id_usuario = str(randint(0, 100))
    usuario = Usuario(id_usuario, nome, idade, cpf)
    usuarios[id_usuario] = usuario
    return {"id": id_usuario, "mensagem": "Usuário criado com sucesso"}

@app.post('/produto')
def criar_produto(nome: str, preco: float, estoque: int):  # <- corrigido aqui
    id_produto = str(randint(0, 100))
    produto = Produto(id_produto, nome, preco, estoque)
    produtos[id_produto] = produto
    return {"id": id_produto, "mensagem": "Produto criado com sucesso"}

@app.post('/carrinho')
def criar_carrinho(id_usuario: str):  # <- corrigido aqui
    if id_usuario not in usuarios:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    id_carrinho = str(randint(0, 100))
    carrinho = Carrinho(id_carrinho, id_usuario)
    carrinhos[id_carrinho] = carrinho
    return {"id": id_carrinho, "mensagem": "Carrinho criado"}

@app.post('/carrinhos/{id_carrinho}/adicionar')
def adicionar_produto(id_carrinho: str, id_produto: str, quantidade: int):
    if id_carrinho not in carrinhos:
        raise HTTPException(status_code=404, detail="Carrinho não encontrado")

    if id_produto not in produtos:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    carrinho = carrinhos[id_carrinho]
    produto = produtos[id_produto]
    carrinho.adicionar_item(produto, quantidade)
    return {"mensagem": f"Produto {produto._nome} adicionado ao carrinho."}

@app.get("/carrinhos/{id_carrinho}")
def ver_carrinho(id_carrinho: str):
    if id_carrinho not in carrinhos:
        raise HTTPException(status_code=404, detail="Carrinho não encontrado")
    return {
        "id": id_carrinho,
        "itens": carrinhos[id_carrinho].listar_itens()
    }
