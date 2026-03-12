from pathlib import Path

pasta = Path("14_3 Filemanager/exercicio3")
caminho_log = pasta / "acesso.log"

if not caminho_log.is_file():
    print("Erro: O arquivo 'acesso.log' não foi encontrado em:")
    print(f"  → {caminho_log.resolve()}")
    exit()

try:
    linhas = caminho_log.read_text(encoding="utf-8").splitlines()
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
    exit()

palavra = input("Digite uma palavra-chave (ex: ERROR, INFO, WARNING, DEBUG): ").strip()

if not palavra:
    print("Nenhuma palavra informada → mostrando todas as linhas.")
    palavra = "" 

palavra_lower = palavra.lower()

encontradas = 0
print(f"\nLinhas que contêm '{palavra}' (ignorando maiúsculas/minúsculas):\n")

for linha in linhas:
    if palavra_lower in linha.lower():
        print(linha.rstrip()) 
        encontradas += 1

if encontradas == 0 and palavra:
    print("Nenhuma linha encontrada com essa palavra-chave.")

print("-" * 70)
print(f"Total de linhas encontradas: {encontradas}")