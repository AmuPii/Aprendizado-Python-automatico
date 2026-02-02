# print("=== Cardápio ===")
# print("1. Pizza")
# print("2. Sushi")
# print("3. Salada")
# print()

# opcao = input("Digite o número do prato desejado: ")

# if opcao == "1":
#     print("Você escolheu: Pizza 🍕")
# elif opcao == "2":
#     print("Você escolheu: Sushi 🍣")
# elif opcao == "3":
#     print("Você escolheu: Salada 🥗")
# else:
#     print("Opção inválida.")



transporte = input("Digite um meio de transporte: ").lower().strip()

if transporte == "carro":
    print("Veículo terrestre")
elif transporte == "bicicleta":
    print("Transporte sustentável")
elif transporte == "avião" or transporte == "helicóptero":
    print("Transporte aéreo")
else:
    print("Transporte desconhecido")