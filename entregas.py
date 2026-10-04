#importando de produtos.py
from produtos import produtos, retirar_estoque, adicionar_estoque

#Lista para armazenar as entregas
entregas = []

#Status válidos de uma entrega
STATUS_VALIDOS = ["Pendente", "Em transporte", "Entregue", "Cancelada"]

def cadastrar_entrega(id_cliente, id_produto, quantidade, endereco):
#Valida se o produto existe pelo id, se encontrou, guarda em produto_encontrado
    produto_encontrado = None
    for produto in produtos:
        if produto["id"] == id_produto:
            produto_encontrado = produto

#Se não foi encontrado, retorna Erro
    if produto_encontrado is None:
        print("Erro: Produto com Id ", id_produto, " não foi encontrado.")
        return None

#Retira do estoque (retorna Erro se o produto não está disponível na quantidade especificada)
    if not retirar_estoque(id_produto, quantidade):
        print("Erro: Quantidade inválida ou estoque insuficiente.")
        return None

    nova_entrega = {
        "id": len(entregas) + 1,
        "id_cliente": id_cliente,
        "id_produto": id_produto,
        "produto": produto_encontrado["nome"],
        "quantidade": quantidade,
        "endereco": endereco,
        "status": "Pendente"
    }

#Adiciona os dados de nova_entrega na lista entregas, na linha 5
    entregas.append(nova_entrega)
    print("Sucesso: Entrega ", nova_entrega['id'], " cadastrada!")
    return nova_entrega

#lista todas as entregas registradas
def listar_entregas():
    print("-----ENTREGAS CADASTRADAS-----")
    if len(entregas) == 0:
        print("Nenhuma entrega cadastrada no sistema")
    else:
        for entrega in entregas:
            print('Id: ',entrega['id'])
            print('Cliente (Id): ', entrega['id_cliente'])
            print('Produto: ',entrega['produto'], ' |  Quantidade: ', entrega['quantidade'])
            print('Endereço: ',entrega['endereco'])
            print('Status: ', entrega['status'])
            print("-------------------------")

#busca entregas específicas registradas, com base no id
def buscar_entrega(id_entrega):
    for entrega in entregas:
        if entrega["id"] == id_entrega:
            return entrega

#Consulta o status da entrega com base em buscar_entrega
#precisa retornar False se dá erro, porq
def atualizar_status(id_entrega, novo_status):
    if novo_status not in STATUS_VALIDOS:
        print("Erro: Status inválido. Use: 'Pendente', 'Em transporte', 'Entregue' ou  'Cancelada'")
        return False

#Dá erro se a entrega não for encontrada
    entrega = buscar_entrega(id_entrega)
    if entrega is None:
        print("Erro: Entrega com Id ", id_entrega, " não foi encontrada.")
        return False

#Verifica se está cancelada ou entregue
    if entrega["status"] in ["Entregue", "Cancelada"]:
        print("Erro: Entrega já finalizada.")
        return False

#Finnalmente atualiza o Status
    entrega["status"] = novo_status
    print("Sucesso: Entrega ",id_entrega, " agora está '", novo_status, "'.")

#Cancela uma entrega usando id como parÂmetro
def cancelar_entrega(id_entrega):
    entrega = buscar_entrega(id_entrega)
    if entrega is None:
        print("Erro: Entrega com Id ",id_entrega, " não foi encontrada.")

#Se a entrega já foi Entregue ou Cancelada não há como cancelar
    if entrega["status"] in ["Entregue", "Cancelada"]:
        print("Erro: Não é possível cancelar, a entrega está '",entrega['status'],"'.")

#Devolve os produtos ao estoque (Se alguém cancelar os produtos precisam ser devolvidos ao sistema)
    adicionar_estoque(entrega["id_produto"], entrega["quantidade"])
    entrega["status"] = "Cancelada"
    print("Sucesso: Entrega ",id_entrega, " cancelada e estoque devolvido.")