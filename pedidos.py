pedidos = []


def criar_pedido(clientes, produtos):
    print("\n--- NOVO PEDIDO ---")

    nome_cliente = input("Digite o nome do cliente: ")

    cliente_encontrado = None

    for cliente in clientes:
        if cliente["nome"].lower() == nome_cliente.lower():
            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:
        print("Cliente não encontrado.")
        return

    nome_produto = input("Digite o nome do produto: ")

    produto_encontrado = None

    for produto in produtos:
        if produto["nome"].lower() == nome_produto.lower():
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        print("Produto não encontrado.")
        return

    try:
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Digite uma quantidade válida.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    if produto_encontrado["estoque"] < quantidade:
        print("Estoque insuficiente.")
        return

    valor_total = produto_encontrado["preco"] * quantidade

    numero_pedido = len(pedidos) + 1

    pedido = {
        "numero": numero_pedido,
        "cliente": cliente_encontrado["nome"],
        "produto": produto_encontrado["nome"],
        "quantidade": quantidade,
        "valor_total": valor_total,
        "status": "Pedido realizado"
    }

    pedidos.append(pedido)

    # Diminui o estoque
    produto_encontrado["estoque"] -= quantidade

    print("\nPedido realizado com sucesso!")
    print(f"Número do pedido: {numero_pedido}")
    print(f"Cliente: {cliente_encontrado['nome']}")
    print(f"Produto: {produto_encontrado['nome']}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor total: R$ {valor_total:.2f}")


def listar_pedidos():
    print("\n--- LISTA DE PEDIDOS ---")

    if len(pedidos) == 0:
        print("Nenhum pedido cadastrado.")
        return

    for pedido in pedidos:
        print("---------------------------")
        print(f"Pedido: {pedido['numero']}")
        print(f"Cliente: {pedido['cliente']}")
        print(f"Produto: {pedido['produto']}")
        print(f"Quantidade: {pedido['quantidade']}")
        print(f"Valor total: R$ {pedido['valor_total']:.2f}")
        print(f"Status: {pedido['status']}")


def buscar_pedido():
    print("\n--- BUSCAR PEDIDO ---")

    try:
        numero = int(input("Digite o número do pedido: "))
    except ValueError:
        print("Número inválido.")
        return

    for pedido in pedidos:
        if pedido["numero"] == numero:
            print("\nPedido encontrado:")
            print(f"Número: {pedido['numero']}")
            print(f"Cliente: {pedido['cliente']}")
            print(f"Produto: {pedido['produto']}")
            print(f"Quantidade: {pedido['quantidade']}")
            print(f"Valor total: R$ {pedido['valor_total']:.2f}")
            print(f"Status: {pedido['status']}")
            return

    print("Pedido não encontrado.")


def alterar_status():
    print("\n--- ALTERAR STATUS DO PEDIDO ---")

    try:
        numero = int(input("Digite o número do pedido: "))
    except ValueError:
        print("Número inválido.")
        return

    for pedido in pedidos:
        if pedido["numero"] == numero:

            print("\n1 - Pedido realizado")
            print("2 - Em preparação")
            print("3 - Em transporte")
            print("4 - Entregue")

            opcao = input("Escolha o novo status: ")

            if opcao == "1":
                pedido["status"] = "Pedido realizado"

            elif opcao == "2":
                pedido["status"] = "Em preparação"

            elif opcao == "3":
                pedido["status"] = "Em transporte"

            elif opcao == "4":
                pedido["status"] = "Entregue"

            else:
                print("Opção inválida.")
                return

            print("Status atualizado com sucesso.")
            return

    print("Pedido não encontrado.")