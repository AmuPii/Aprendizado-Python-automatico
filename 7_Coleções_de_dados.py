animais = ["Gato", "Cachorro", "Papagaio"]

print(f"O primeiro animal é: {animais[0]}")

print(f"O último animal é: {animais[-1]}")



livros = ["Python", "Java", "C++"]

livros.append("JavaScript")

livros.remove("Java")

livros[0] = "Go"

print(f"Lista final: {livros}")
print(f"Tamanho da lista: {len(livros)}")



nomes = [ "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fernando", "Giovana", "Hugo", "Isabela", "João", "Carla", "Lucas", "Mariana", "Nuno", "Olivia", "João", "Pedro", "Carla", "Rafael", "Ana" ]

qtd_carla = nomes.count("Carla")

indice_carla = nomes.index("Carla")

print(f"A Carla aparece {qtd_carla} vezes.")
print(f"A primeira aparição é no índice {indice_carla}.")