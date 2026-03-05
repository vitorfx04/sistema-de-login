# Gerenciamento de Usuários em Python

Este projeto é um sistema simples de gerenciamento de usuários em Python que permite o registro e login de usuários utilizando um arquivo JSON para armazenar as credenciais.

## Funcionalidades

- Registrar novos usuários.
- Realizar login com usuário e senha.
- Armazenar os dados de usuários em um arquivo JSON.

## Estrutura do Projeto

O projeto consiste em um único arquivo Python que realiza as seguintes operações:

### 1. Importação de Bibliotecas

```python
import json
```
Utiliza-se a biblioteca `json` para armazenar e recuperar os dados dos usuários.

### 2. Variáveis Globais

```python
ARQUIVO_USUARIOS = "usuarios.json"
```
Define o nome do arquivo JSON onde os dados serão armazenados.

### 3. Funções do Sistema

#### Carregar Usuários
```python
def carregar_usuarios():
    try:
        with open(ARQUIVO_USUARIOS, "r") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
```
Esta função tenta carregar os usuários armazenados no arquivo JSON. Se o arquivo não existir ou estiver corrompido, retorna um dicionário vazio.

#### Salvar Usuários
```python
def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)
```
Esta função salva o dicionário de usuários no arquivo JSON.

#### Registrar Usuário
```python
def register_user(usuarios):
```
Esta função solicita ao usuário um nome de usuário e senha, verifica se já existe e salva os dados no arquivo JSON caso esteja tudo correto.

Passos:
1. Solicita o nome do usuário.
2. Verifica se o nome de usuário já existe.
3. Solicita a confirmação do nome de usuário.
4. Solicita a senha e confirmação da senha.
5. Salva os dados no arquivo JSON.

#### Login
```python
def login(usuarios):
```
Esta função solicita ao usuário seu nome e senha, verifica se estão corretos e permite o login.

Passos:
1. Solicita o nome do usuário.
2. Verifica se o nome de usuário existe.
3. Solicita a senha.
4. Verifica se a senha está correta.

### 4. Loop Principal

O sistema apresenta um menu interativo que permite ao usuário escolher entre:
- Registrar um novo usuário.
- Fazer login.
- Sair do programa.

```python
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
```

## Como Usar

1. Execute o script Python: `python index.py`
2. Escolha uma das opções no menu.
3. Para registrar um usuário, insira um nome e uma senha.
4. Para fazer login, informe um usuário já registrado e sua senha.

## Melhorias Futuras

- Implementar hashing de senhas para aumentar a segurança.
- Criar um sistema de recuperação de senha.
- Desenvolver uma interface gráfica para facilitar o uso.
- Adicionar log de tentativas de login para monitoramento.

## Autor

Desenvolvido por [Vitor Baratto].

