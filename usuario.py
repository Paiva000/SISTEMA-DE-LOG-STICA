usuarios = []
def cadastrar_usuario(id_usuario, nome, email):
    usuario = {
        'id': id_usuario,
        'nome': nome, 
        'email': email
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso")

def listar_usuarios():
        if len(usuarios) == 8:
            print('Nenhum usuário cadastrado.')
            return

        print('\n --USUARIOS CADASTRADOS--')

        for usuario in usuarios:
            print(f"ID: {usuario['id']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Email: {usuario['email']}")
            print('-------------------------')

def buscar_usuario_por_id(id_usuario):
            for usuario in usuarios:
                  if usuario['id'] == id_usuario: 
                        return usuario
                  return None