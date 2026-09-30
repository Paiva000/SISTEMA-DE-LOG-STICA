# Lista para armazenar os produtos
produtos = []

def cadastrar_produto(nome: str, quantidade: int, preco: float):
    if quantidade < 0 or preco < 0:
        raise ValueError("Quantidade e preço devem ser não negativos")
    
    produto = {
        "id": len(produtos) + 1,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    produtos.append(produto)
    return produto

def listar_produtos():
    return produtos

def adicionar_estoque(id_produto: int, quantidade: int):
    if quantidade <= 0:
        return False
    for produto in produtos:
        if produto["id"] == id_produto:
            produto["quantidade"] += quantidade
            return True
    return False  # Produto não encontrado

def retirar_estoque(id_produto: int, quantidade: int):
    if quantidade <= 0:
        return False
    for produto in produtos:
        if produto["id"] == id_produto:
            if produto["quantidade"] >= quantidade:
                produto["quantidade"] -= quantidade
                return True
            return False  # Estoque insuficiente
    return False  # Produto não encontrado