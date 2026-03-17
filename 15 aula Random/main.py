import random

convidados = ["Ana", "Lucas", "João", "Marina", "Pedro", "Carla", "Ricardo", "Fernanda"]
premios = ["Bicicleta", "Tablet", "Fone de ouvido", "Livro", "Camisa"]

Sorteio_convidado = random.sample(convidados, k=5)
Sorteio_premio = random.sample(premios, k=5)

Contador = 0

while Contador < 5:
    convidado = Sorteio_convidado[Contador]
    premio = Sorteio_premio[Contador]
    print(f'o convidado "{convidado}" ganhou "{premio}"')
    Contador += 1