lista_cliente = []

def cadastrar_cliente(id_cliente, nome, endereco):
    novo_cliente = {"id": id_cliente, "nome": nome, "endereco": endereco}
    lista_cliente.append(novo_cliente)
    print(f"Sucesso: O cliente {nome} foi cadastrado!")

def lista_cliente():
    print("Lista de Clientes")
    if len(lista_cliente) == 0:
        print("Nenhum cliente cadastrado no sistema")
    else:
        for cliente in lista_cliente:
            print(f"Id: {cliente["id"]}, Nome: {cliente["nome"]}, Endereço: {cliente["endereco"]}")

def busca_cliente(id_cliente):
    for cliente in lista_cliente:
        if cliente["id"] == id_cliente:
            print(f"Cliente Encontrado: {cliente["nome"]}, Endereço: {cliente["endereco"]}")
            return cliente
        print(f"Erro: Cliente com Id{id_cliente} não foi encontrado.")

def remover_cliente(id_cliente):
    for cliente in lista_cliente:
        if cliente["id"] == id_cliente:
            lista_cliente.remove(cliente)
            print(f"Sucesso: Cliente com Id {id_cliente} foi removido.")
        print(f"Erro: Não é possivel remover o cliente com o Id{id_cliente} Não existe.")                    