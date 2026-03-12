from pathlib import Path
import shutil
from datetime import datetime

Arquivo = Path("14_3 Filemanager/exercicio1")

relatorio = Arquivo / "relatorio.txt"
relatorio.touch()

with open(relatorio, "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Relatório criado em: {datetime.now()}\n")
    arquivo.write("Estou aprendendo Python!")
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    arquivo.write(f"\nÚltima modificação: {agora}")