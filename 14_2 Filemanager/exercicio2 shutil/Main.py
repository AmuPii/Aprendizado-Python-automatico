import shutil 
from pathlib import Path

PASTA_BASE = Path("14_2 Filemanager/exercicio2 shutil")

PASTA_BASE.mkdir(parents=True, exist_ok=True)

relatorio = PASTA_BASE / "relatorio.txt"
relatorio.touch(exist_ok=True)

pasta_antigos = PASTA_BASE / "relatorios_antigos"
pasta_antigos.mkdir(exist_ok=True)

destino = pasta_antigos / "relatorioBackup.txt"

shutil.move(relatorio, destino)
