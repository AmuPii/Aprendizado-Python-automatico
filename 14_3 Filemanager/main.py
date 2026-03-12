from pathlib import Path
pasta = Path("14_3 Filemanager/arquivo.txt")
arquivo = open(pasta)
conteudo = arquivo.read()

print(conteudo)
arquivo.close()

with open (pasta, "r+", encoding="utf-8") as arquivo:
    arquivo.write("Olá, mundão! ")
    arquivo.seek(0)
    print(arquivo.read())