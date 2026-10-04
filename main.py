from usuario import cadastrar_usuario, listar_usuarios, buscar_usuario_por_id
from clientes import lista_clientes, cadastrar_cliente, listar_clientes, busca_cliente, remover_cliente
from produtos import produtos, cadastrar_produto, listar_produtos, adicionar_estoque, retirar_estoque
from pedidos import criar_pedido, listar_pedidos, buscar_pedido, alterar_status
from entregas import cadastrar_entrega, listar_entregas, buscar_entrega, atualizar_status, cancelar_entrega


def menu():
    while True:
        print("\n========== SISTEMA DE LOGÍSTICA ==========")

        print("\n--- USUÁRIOS ---")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Buscar usuário")

        print("\n--- CLIENTES ---")
        print("4 - Cadastrar cliente")
        print("5 - Listar clientes")
        print("6 - Buscar cliente")
        print("7 - Remover cliente")

        print("\n--- PRODUTOS ---")
        print("8 - Cadastrar produto")
        print("9 - Listar produtos")
        print("10 - Adicionar estoque")
        print("11 - Retirar estoque")

        print("\n--- PEDIDOS ---")
        print("12 - Criar pedido")
        print("13 - Listar pedidos")
        print("14 - Buscar pedido")
        print("15 - Alterar status do pedido")

        print("\n--- ENTREGAS ---")
        print("16 - Cadastrar entrega")
        print("17 - Listar entregas")
        print("18 - Buscar entrega")
        print("19 - Atualizar status da entrega")
        print("20 - Cancelar entrega")

        print("\n0 - Sair")

        opcao = input("Escolha uma opção: ")

        # USUÁRIOS
        if opcao == "1":
            id_usuario = input("Digite o ID do usuário: ")
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            cadastrar_usuario(id_usuario, nome, email)

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            id_usuario = input("Digite o ID do usuário: ")
            usuario = buscar_usuario_por_id(id_usuario)
            if usuario:
                print("Usuário encontrado:")
                print(f"ID: {usuario['id']}")
                print(f"Nome: {usuario['nome']}")
                print(f"Email: {usuario['email']}")

        # CLIENTES
        elif opcao == "4":
            id_cliente = input("Digite o ID do cliente: ")
            nome = input("Digite o nome do cliente: ")
            endereco = input("Digite o endereço do cliente: ")
            cadastrar_cliente(id_cliente, nome, endereco)

        elif opcao == "5":
            listar_clientes()

        elif opcao == "6":
            id_cliente = input("Digite o ID do cliente: ")
            cliente = busca_cliente(id_cliente)
            if cliente:
                print("Cliente encontrado:")
                print(f"ID: {cliente['id']}")
                print(f"Nome: {cliente['nome']}")
                print(f"Endereço: {cliente['endereco']}")

        elif opcao == "7":
            id_cliente = input("Digite o ID do cliente: ")
            remover_cliente(id_cliente)

        # PRODUTOS
        elif opcao == "8":
            nome = input("Digite o nome do produto: ")
            try:
                quantidade = int(input("Digite a quantidade: "))
                preco = float(input("Digite o preço: R$ "))
                produto = cadastrar_produto(nome, quantidade, preco)
                if produto:
                    print(f"Produto {produto['nome']} cadastrado com sucesso!")
            except ValueError:
                print("Erro: Digite valores numéricos válidos para quantidade e preço.")

        elif opcao == "9":
            lista = listar_produtos()
            print("--- PRODUTOS CADASTRADOS ---")
            if not lista:
                print("Nenhum produto cadastrado.")
            else:
                for produto in lista:
                    print("-------------------------")
                    print(f"ID: {produto['id']}")
                    print(f"Nome: {produto['nome']}")
                    print(f"Quantidade: {produto['quantidade']}")
                    print(f"Preço: R$ {produto['preco']:.2f}")

        elif opcao == "10":
            try:
                id_produto = int(input("Digite o ID do produto: "))
                quantidade = int(input("Quantidade a adicionar: "))
                if adicionar_estoque(id_produto, quantidade):
                    print("Estoque atualizado com sucesso!")
                else:
                    print("Não foi possível adicionar estoque.")
            except ValueError:
                print("Erro: Digite um ID e quantidade numéricos.")

        elif opcao == "11":
            try:
                id_produto = int(input("Digite o ID do produto: "))
                quantidade = int(input("Quantidade a retirar: "))
                if retirar_estoque(id_produto, quantidade):
                    print("Estoque retirado com sucesso!")
                else:
                    print("Produto inexistente ou estoque insuficiente.")
            except ValueError:
                print("Erro: Digite um ID e quantidade numéricos.")

        # PEDIDOS
        elif opcao == "12":
            criar_pedido(lista_clientes, produtos)

        elif opcao == "13":
            listar_pedidos()

        elif opcao == "14":
            buscar_pedido()

        elif opcao == "15":
            alterar_status()

        # ENTREGAS
        elif opcao == "16":
            try:
                id_cliente = input("Digite o ID do cliente: ")
                id_produto = int(input("Digite o ID do produto: "))
                quantidade = int(input("Digite a quantidade: "))
                endereco = input("Digite o endereço da entrega: ")
                cadastrar_entrega(id_cliente, id_produto, quantidade, endereco)
            except ValueError:
                print("Erro: O ID do produto e a quantidade devem ser números.")

        elif opcao == "17":
            listar_entregas()

        elif opcao == "18":
            try:
                id_entrega = int(input("Digite o ID da entrega: "))
                entrega = buscar_entrega(id_entrega)
                if entrega:
                    print("Entrega encontrada:")
                    print(f"ID: {entrega['id']}")
                    print(f"Cliente: {entrega['id_cliente']}")
                    print(f"Produto: {entrega['produto']}")
                    print(f"Quantidade: {entrega['quantidade']}")
                    print(f"Endereço: {entrega['endereco']}")
                    print(f"Status: {entrega['status']}")
            except ValueError:
                print("Erro: Digite um número de ID válido.")

        elif opcao == "19":
            try:
                id_entrega = int(input("Digite o ID da entrega: "))
                print("Status disponíveis:")
                print("Pendente")
                print("Em transporte")
                print("Entregue")
                print("Cancelada")
                novo_status = input("Digite o novo status: ")
                atualizar_status(id_entrega, novo_status)
            except ValueError:
                print("Erro: Digite um número de ID válido.")

        elif opcao == "20":
            try:
                id_entrega = int(input("Digite o ID da entrega: "))
                cancelar_entrega(id_entrega)
            except ValueError:
                print("Erro: Digite um número de ID válido.")

        # SAIR
        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

        input("Pressione Enter para continuar...")    

if __name__ == "__main__":
    menu()