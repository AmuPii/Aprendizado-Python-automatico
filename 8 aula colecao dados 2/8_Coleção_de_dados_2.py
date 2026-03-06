livro = {
    "titulo": "Dom Quixote",
    "autor": "Miguel de Cervantes",
    "ano": 1605
}

print(f"Título: {livro['titulo']}")
print(f"Autor:  {livro['autor']}")
print(f"Ano:    {livro['ano']}")




nome_digitado = input("Digite seu nome: ")
idade_digitada = int(input("Digite sua idade: "))

usuario = {
    "nome": nome_digitado,
    "idade": idade_digitada
}

if usuario["idade"] >= 18:
    print(f"✅ Acesso liberado para {usuario['nome']}")
else:
    print(f"⛔ Acesso negado para {usuario['nome']}")



credenciais_sistema = {
    "usuario": "herick",
    "senha": "12345"
}

print("--- SISTEMA DE LOGIN ---")

user_input = input("Digite seu usuário: ")
pass_input = input("Digite sua senha: ")

tentativa_login = {
    "usuario": user_input,
    "senha": pass_input
}

if (tentativa_login["usuario"] == credenciais_sistema["usuario"]) and \
   (tentativa_login["senha"] == credenciais_sistema["senha"]):
    print("✅ Login bem-sucedido! Bem-vindo(a).")
else:
    print("❌ Usuário ou senha incorretos.")