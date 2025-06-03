# Projeto API de E-commerce
Este projeto é uma API REST simples desenvolvida com FastAPI para gerenciar usuários, produtos e carrinhos de compras, simulando a base de um sistema de e-commerce.

# Funcionalidades
Cadastro de usuários: criação de usuários com nome, idade e CPF.

Cadastro de produtos: criação de produtos com nome, preço e estoque.

Criação de carrinhos: associação de um carrinho a um usuário específico.

Adicionar produtos ao carrinho: adicionar itens em quantidade ao carrinho do usuário.

Visualização do carrinho: listar todos os itens adicionados ao carrinho.

# Estrutura do Projeto
ProjetoApi/
Contém os módulos usuario.py, produto.py e carrinho.py que definem as classes do domínio.

main.py
Contém as rotas da API e a lógica principal.

# Acesse a documentação interativa automática:
http://localhost:8000/docs (Swagger UI)
