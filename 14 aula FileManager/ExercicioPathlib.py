from pathlib import Path

arquivos = ["dados1.txt", "dados2.txt", "dados3.txt"]

Estrutura = [
    "14 aula FileManager/dados/entrada",
    "14 aula FileManager/dados/saida",
    "14 aula FileManager/relatorios"
]

for caminho in Estrutura:
    Path(caminho).mkdir(parents=True, exist_ok=True)

for arquivo in arquivos:
    Path(f"14 aula FileManager/dados/entrada/{arquivo}").touch

for arquivo in Path("14 aula FileManager/dados/entrada").glob("*.txt"):
    print(arquivo.name)

    