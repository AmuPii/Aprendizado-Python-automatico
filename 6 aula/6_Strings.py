# 1. Pede ao usuário para digitar uma palavra
palavra = input("Digite uma palavra: ")

# 2. Exibe a primeira letra (índice 0)
print(f"A primeira letra é: {palavra[0]}")

# 3. Exibe a última letra (índice -1)
print(f"A última letra é: {palavra[-1]}")





frase = input("Digite uma frase: ")

inicio = int(input("Digite o índice de início: "))
fim = int(input("Digite o índice de fim: "))

trecho = frase[inicio:fim]

print(f"O trecho recortado é: {trecho}")






mensagem = input("Escreva sua mensagem: ")

if "bomba" in mensagem.lower():
    print("🚨 ALERTA: Palavra proibida detectada!")
else:
    print("Mensagem aprovada.")




frase_baguncada = "    @prendendo @ progr@m@r    "

passo_1 = frase_baguncada.strip()

passo_2 = passo_1.replace("@", "a")

resultado_final = passo_2.title()

print(f"Original: '{frase_baguncada}'")
print(f"Limpa:    '{resultado_final}'")