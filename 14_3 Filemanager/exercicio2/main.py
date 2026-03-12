from pathlib import Path
import shutil

Arquivo = Path("14_3 Filemanager/exercicio2")

Mensagem = Arquivo / "mensagem.txt"
Mensagem.touch()

with open(Mensagem, "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, este é um arquivo de mensagem!")
    arquivo.write("\nEstou aprendendo a manipular arquivos com Python.")

with open(Mensagem, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    contador_letras = len(conteudo.replace(" ", ""))
    print(f"O número de letras no arquivo é: {contador_letras}")

