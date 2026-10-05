produtos = []

def cadastrar_produto(nome: str, quantidade: int, preco: float):
    # Validação simples: se quantidade ou preço forem negativos, recusa o cadastro
    if quantidade < 0 or preco < 0:
        return None  # Retorna None para indicar que o cadastro não foi realizado
    
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