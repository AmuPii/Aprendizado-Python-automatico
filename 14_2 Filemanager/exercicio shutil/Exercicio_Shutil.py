import shutil 
import pathlib 
import os

caminho = pathlib.Path("14_2 Filemanager/exercicio shutil/imagens")

caminho.mkdir(exist_ok=True)

Novapasta = pathlib.Path("14_2 Filemanager/exercicio shutil/backup")
Novapasta.mkdir(exist_ok=True)


for item in os.listdir("14_2 Filemanager/exercicio shutil/imagens"):
	s = os.path.join("14_2 Filemanager/exercicio shutil/imagens", item)
	d = os.path.join("14_2 Filemanager/exercicio shutil/backup", item)
	if os.path.isfile(s):
		shutil.copy2(s, d)


for item in os.listdir("14_2 Filemanager/exercicio shutil/imagens"):
	s = os.path.join("14_2 Filemanager/exercicio shutil/imagens", item)
	d = os.path.join("14_2 Filemanager/exercicio shutil/backup", item)
	shutil.move(s, d)



