from pathlib import Path
import shutil

base = Path("14_2 Filemanager/exercicio3")

pasta_extraido = base / "extraido"
pasta_extraido.mkdir(exist_ok=True)

zip_path = base / "arquivos_secretos.zip"

shutil.unpack_archive(zip_path, pasta_extraido)

print("Arquivos extraídos na pasta extraido/:")
for item in pasta_extraido.rglob("*"):
    if item.is_file():
        print(f"  • {item.name}")