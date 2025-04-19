import json
import hashlib
import os

ARQUIVO_USUARIOS = "usuarios.json"

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        try:
            with open(ARQUIVO_USUARIOS, "r") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de usuários.")
    return {}

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def registrar_usuario(usuarios):
    print("\n--- Registro de Novo Usuário ---")
    user = input("Digite seu nome de usuário: ").strip()

    if not user:
        print("Nome de usuário não pode estar vazio!")
        return

    if user in usuarios:
        print("Usuário já existe! Tente outro nome.")
        return

    user_confirm = input("Confirme seu nome de usuário: ").strip()
    if user != user_confirm:
        print("Os nomes de usuário não coincidem!")
        return

    senha = input("Digite sua senha: ").strip()
    senha_confirm = input("Confirme sua senha: ").strip()

    if not senha:
        print("Senha não pode estar vazia!")
        return

    if senha != senha_confirm:
        print("As senhas não coincidem!")
        return

    email = input("Digite seu e-mail: ").strip()
    nome = input("Digite seu nome completo: ").strip()

    usuarios[user] = {
        "senha": gerar_hash(senha),
        "email": email,
        "nome": nome
    }

    salvar_usuarios(usuarios)
    print("✅ Usuário cadastrado com sucesso!")

def login(usuarios):
    print("\n--- Login ---")
    user = input("Digite seu nome de usuário: ").strip()

    if user not in usuarios:
        print("Usuário não encontrado!")
        return

    tentativas = 3
    while tentativas > 0:
        senha = input("Digite sua senha: ").strip()
        if usuarios[user]["senha"] == gerar_hash(senha):
            print(f"✅ Login bem-sucedido! Bem-vindo(a), {usuarios[user]['nome']}")
            return
        else:
            tentativas -= 1
            print(f"Senha incorreta! Tentativas restantes: {tentativas}")
    print("⚠️ Muitas tentativas. Tente novamente mais tarde.")

def menu():
    usuarios = carregar_usuarios()
    while True:
        print("\n--- MENU ---")
        print("1 - Registrar")
        print("2 - Login")
        print("3 - Sair")
        opc = input("Escolha uma opção: ").strip()

        if opc == "1":
            registrar_usuario(usuarios)
        elif opc == "2":
            login(usuarios)
        elif opc == "3":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
