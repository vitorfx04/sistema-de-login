import json

ARQUIVO_USUARIOS = "usuarios.json"

def carregar_usuarios():
    try:
        with open(ARQUIVO_USUARIOS, "r") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def register_user(usuarios):
    user = input("Digite seu usuário: ")

    if user in usuarios:
        print("Usuário já existe! Tente novamente.")
        return

    user_confirm = input("Confirme seu usuário: ")
    if user != user_confirm:
        print("Os usuários não coincidem! Tente novamente.")
        return

    senha = input("Digite sua senha: ")
    senha_confirm = input("Confirme sua senha: ")

    if senha != senha_confirm:
        print("As senhas não coincidem! Tente novamente.")
        return

    #Armazena a senha do usuario
    usuarios[user] = senha  
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")

def login(usuarios):
    user = input("Digite seu usuário: ")

    if user not in usuarios:
        print("Usuário não encontrado!")
        return

    senha = input("Digite sua senha: ")

    if usuarios[user] == senha:
        print("Login bem-sucedido! Bem-vindo,", user)
    else:
        print("Senha incorreta!")

usuarios = carregar_usuarios()

while True:
    print("\n1 - Registrar\n2 - Login\n3 - Sair")
    opc = input("Escolha uma opção: ")

    if opc == "1":
        register_user(usuarios)
    elif opc == "2":
        login(usuarios)
    elif opc == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")
