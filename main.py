from usuario import cadastrar_usuario, listar_usuarios, buscar_usuario_por_id1


def menu():
    while True:
        print("\n ===== SISTEMA DE LOGÍSTICA =====")
        print("1 - Cadastrar Usuário")
        print("2 - Listar Usuários")
        print("3 - Buscar Usuário")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            id_usuario = input("Digite o ID do usuário: ")
            nome = input("Digite o nome do usuario:")
            email = input("Digite o email do usuario: ")

            cadastrar_usuario(id_usuario, nome, email)

        elif opcao == '2':
            listar_usuarios()

        elif opcao == "3":
            id_usuario = int(input("Digite o ID do usuário: "))

            usuario = buscar_usuario_por_id(id_usuario)

            if usuario: 
                print("\nUsuario encontrado:")
                print(f"ID: {usuario['id']}")
                print(f"Nome: {usuario['nome']}")
                print(f"Email: {usuario['email']}")
            else: 
                print("Usuário não encontrado.")

        elif opcao =='0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
