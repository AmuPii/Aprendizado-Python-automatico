
# numero = 10

# while numero >= 1:
#     print(numero)
#     numero = numero - 1

# print("FIM")



# soma = 0
# contador = 1

# print("Vou pedir 5 números para somar\n")

# while contador <= 5:
#     numero = float(input(f"Digite o {contador}º número: "))
#     soma = soma + numero
#     contador = contador + 1

# print("\nA soma de todos os números é:", soma)



# total = 0

# print("Cofrinho: digite valores (0 para parar)\n")

# while True:
#     try:
#         valor = float(input("R$ "))
#         if valor == 0:
#             break
#         if valor > 0:
#             total += valor
#             print(f"  total → R$ {total:.2f}")
#         else:
#             print("Só valores positivos!")
#     except:
#         print("Digite um número válido")

# print(f"\nVocê economizou: R$ {total:.2f} ")



pizza = 0
hamburguer = 0

while True:
    try:
        op = int(input("1.Pizza  2.Hambúrguer  3.Sair → "))
        if op == 1:
            pizza += 1
        elif op == 2:
            hamburguer += 1
        elif op == 3:
            break
        else:
            print("Apenas 1, 2 ou 3!")
    except:
        print("Digite um número!")

print("\nResultado:")
print(f"Pizza     : {pizza}")
print(f"Hambúrguer: {hamburguer}")
if pizza > hamburguer:
    print("→ Pizza ganhou!")
elif hamburguer > pizza:
    print("→ Hambúrguer ganhou!")
else:
    print("→ Empate!")