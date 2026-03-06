# from modulos import mensagens, matematica

# #Peça ao usuário um número e mostre o dobro e a metade

# #Dê boas-vindas usando o nome digitado

# numero = float(input("Digite um número: "))
# print(f"O dobro de {numero} é {matematica.dobro(numero)}")
# print(f"A metade de {numero} é {matematica.metade(numero)}")

# nome = input("Digite seu nome: ")
# print(mensagens.boas_vindas(nome))

# from meu_pacote import formatador, numeros

# texto = input("Digite um texto: ")
# print(formatador.cauxa_alta(texto))

# nnumero = int(input("Digite um número para verificar se é par: "))
# if numeros.eh_par(nnumero):
#     print(f"{nnumero} é par.")



from perfil import usuario, validacao

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if validacao.idade_valida(idade):
    perfil = usuario.criar_perifl(nome, idade)
    print("Perfil criado com sucesso!")
    print(perfil)
else:
    print("Idade inválida. O perfil não pode ser criado.")

