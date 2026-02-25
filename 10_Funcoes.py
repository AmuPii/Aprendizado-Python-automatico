# # Função que calcula o quadrado de um número
# def quadrado(numero):
#     """
#     Recebe um número e retorna o seu quadrado.
#     Exemplo: quadrado(5) → 25
#     """
#     return numero * numero
#     # ou: return numero ** 2  (outra forma comum)



# print("Vamos calcular o quadrado de um número!\n")


# try:
#     valor = float(input("Digite um número: "))
    
   
#     resultado = quadrado(valor)
    
    
#     print(f"\nO quadrado de {valor} é {resultado}")
   

# except ValueError:
#     print("Por favor, digite um número válido (ex: 4.5, 10, -3)")





#     def apresentar_pessoa(nome, idade):
#     return f"Nome: {nome} | Idade: {idade} anos"


# # Usando a função
# print(apresentar_pessoa("Carlos", 28))
# print(apresentar_pessoa("Beatriz", 37))

# # Com input
# nome = input("Nome: ")
# idade = int(input("Idade: "))
# print(apresentar_pessoa(nome, idade))



# Função que verifica se um número é par ou ímpar
def verificar_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    # Forma alternativa (mais curta):
    # return "Par" if numero % 2 == 0 else "Ímpar"


# Programa principal
print("Verificador de Par ou Ímpar\n")

try:
    # Pede o número ao usuário
    num = float(input("Digite um número: "))
    
    # Chama a função
    resultado = verificar_par(num)
    
    # Mostra o resultado de forma clara
    print(f"\nO número {num} é: {resultado}")
    
    # Exemplo de mensagem mais amigável:
    if resultado == "Par":
        print("→ Esse número é divisível por 2!")
    else:
        print("→ Esse número não é divisível por 2!")

except ValueError:
    print("Por favor, digite um número válido (ex: 4, 7.5, -2)")


