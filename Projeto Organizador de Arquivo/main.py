import shutil
from pathlib import Path
from datetime import datetime

pasta_organizada = Path("Arquivos_Organizados")

Origem = Path("Projeto Organizador de Arquivo/organizador")

arquivo_log = Path("Registro.log")

arquivo_qtd = 0

extensoes_encontradas = []

for arquivo in Path(Origem).iterdir():
    arquivo_qtd += 1
    extensao = arquivo.suffix[1:]
    if extensao not in extensoes_encontradas:
        extensoes_encontradas.append(extensao)

    subpastas = pasta_organizada/extensao
    if not subpastas.exists():
        subpastas.mkdir(exist_ok=True, parents=True)

    shutil.copy(arquivo, subpastas/arquivo.name)
    with open(arquivo_log, "a", encoding="utf-8") as log:
        agora = datetime.now()
        log.write(agora.strftime(f'%Y/%m/%d %H:%M:%S - movido o arquivo {arquivo.name} para a pasta {subpastas}\n'))

print(f"{arquivo_qtd} arquivos organizados com sucesso.")
print(f"Extensões encontradas: ")
for extensao in extensoes_encontradas:
    print(extensao)