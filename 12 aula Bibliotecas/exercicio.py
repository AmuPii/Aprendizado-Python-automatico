import random

numero = random.randint(1, 10)
tentativas = 0

print("Adivinhe o número (1-10):")

while True:
    palpite = int(input("→ "))
    tentativas += 1
    
    if palpite > numero:
        print("Muito alto!")
    elif palpite < numero:
        print("Muito baixo!")
    else:
        print(f"Acertou em {tentativas} tentativas!")
        break