usuarios = []

def projeto(nome, idade=None):
    if idade:
        return f"Olá, {nome}! Você tem {idade} anos."
    return f"Olá, {nome}!"

def projeto(nome, idade=None):
    if idade:
        return f"Olá, {nome}! Você tem {idade} anos."
    return f"Olá, {nome}!"

def criar_usuario(nome, email, idade=None):
    novo_id = len(usuarios) + 1
    usuario = {"id": novo_id, "nome": nome, "email": email, "idade": idade}
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")
    print(projeto(nome, idade))

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    for user in usuarios:
        print(user)

def atualizar_usuario(user_id, nome=None, email=None, idade=None):
    for user in usuarios:
        if user["id"] == user_id:
            if nome: user["nome"] = nome
            if email: user["email"] = email
            if idade: user["idade"] = idade
            print("Usuário atualizado:", user)
            return
    print("Usuário não encontrado.")

def deletar_usuario(user_id):
    global usuarios
    usuarios = [user for user in usuarios if user["id"] != user_id]
    print(f"Usuário de ID {user_id} deletado.")

def menu():
    while True:
        print("\n1. Criar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            idade_input = input("Idade (opcional): ")
            idade = int(idade_input) if idade_input else None
            criar_usuario(nome, email, idade)
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            id_user = int(input("ID do usuário: "))
            nome = input("Novo nome (ou Enter): ")
            email = input("Novo email (ou Enter): ")
            idade_input = input("Nova idade (ou Enter): ")
            idade = int(idade_input) if idade_input else None
            atualizar_usuario(id_user, nome or None, email or None, idade)
        elif opcao == "4":
            id_user = int(input("ID do usuário: "))
            deletar_usuario(id_user)
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
