lista_clientes = [] 

def cadastrar_cliente(id_cliente, nome, endereco):
    novo_cliente = {"id": id_cliente, "nome": nome, "endereco": endereco}
    lista_clientes.append(novo_cliente)
    print(f"Sucesso: O cliente {nome} foi cadastrado!")

def listar_clientes():  
    print("Lista de Clientes")
    if len(lista_clientes) == 0:
        print("Nenhum cliente cadastrado no sistema")
    else:
        for cliente in lista_clientes:
            print(f"Id: {cliente['id']}, Nome: {cliente['nome']}, Endereço: {cliente['endereco']}")

def busca_cliente(id_cliente):
    for cliente in lista_clientes:
        if cliente["id"] == id_cliente:
            print(f"Cliente Encontrado: {cliente['nome']}, Endereço: {cliente['endereco']}")
            return cliente
    print(f"Erro: Cliente com Id {id_cliente} não foi encontrado.")

def remover_cliente(id_cliente):
    for cliente in lista_clientes:
        if cliente["id"] == id_cliente:
            lista_clientes.remove(cliente)
            print(f"Sucesso: Cliente com Id {id_cliente} foi removido.")
            return
    print(f"Erro: Não é possível remover o cliente com o Id {id_cliente}. Não existe.")