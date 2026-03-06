from datetime import datetime

TimeNow = datetime.now()

print("A data e hora atual é: ", TimeNow)
if TimeNow.hour < 12:
    print("Bom dia!")
elif TimeNow.hour < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")


# ================================

MonthNow = datetime.now().month

for i in range(1, 13):
    if MonthNow == i:
        print("Estamos no mês: ", i, "e faltam ", 12 - i, " meses para terminar o ano.")

# ================================


def assinatura():
    
    nome = input("Digite seu nome: ")
    data_atual = datetime.now()
    print("assinatura de: ", nome, " em data:", data_atual.strftime("%d de %B de %Y às %H:%M:%S"))

assinatura()