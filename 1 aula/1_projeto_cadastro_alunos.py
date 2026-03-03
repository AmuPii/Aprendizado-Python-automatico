def exibir_menu():
    """Exibe as opções do menu principal."""
    print("\n" + "="*30)
    print("SISTEMA DE CADASTRO ESCOLAR")
    print("="*30)
    print("1. Adicionar aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno pelo nome")
    print("4. Remover aluno")
    print("5. Mostrar média geral das notas")
    print("6. Sair")
    print("="*30)

def adicionar_aluno(lista_alunos):
    """Adiciona um novo aluno à lista com validação de dados."""
    nome = input("Digite o nome do aluno: ").strip()
    
    
    while True:
        try:
            idade = int(input(f"Digite a idade de {nome}: "))
            if idade <= 0:
                print(" A idade deve ser maior que zero. Tente novamente.")
                continue
            break
        except ValueError:
            print(" Erro: Por favor, digite um número inteiro válido para a idade.")
    
    
    while True:
        try:
            nota = float(input(f"Digite a nota de {nome} (0 a 10): "))
            if 0 <= nota <= 10:
                break
            else:
                print(" A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print(" Erro: Por favor, digite um número válido para a nota.")
    
    
    aluno = {"nome": nome, "idade": idade, "nota": nota}
    lista_alunos.append(aluno)
    print(f"\n Aluno(a) '{nome}' adicionado com sucesso!")

def listar_alunos(lista_alunos):
    """Exibe todos os alunos cadastrados."""
    if not lista_alunos:
        print("\n Nenhum aluno cadastrado no momento.")
        return

    print("\n LISTA DE ALUNOS:")
    for i, aluno in enumerate(lista_alunos, start=1):
        print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']:.1f}")

def buscar_aluno(lista_alunos):
    """Busca um aluno específico pelo nome."""
    if not lista_alunos:
        print("\n Não há alunos cadastrados para buscar.")
        return

    nome_busca = input("Digite o nome do aluno que deseja buscar: ").strip().lower()
    
    for aluno in lista_alunos:
        if aluno['nome'].lower() == nome_busca:
            print("\n ALUNO ENCONTRADO:")
            print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']:.1f}")
            return 
            
    print(f"\n❌ Aluno(a) '{nome_busca}' não encontrado.")

def remover_aluno(lista_alunos):
    """Remove um aluno da lista usando o nome."""
    if not lista_alunos:
        print("\n📭 Não há alunos cadastrados para remover.")
        return

    nome_remover = input("Digite o nome do aluno que deseja remover: ").strip().lower()
    
    for aluno in lista_alunos:
        if aluno['nome'].lower() == nome_remover:
            lista_alunos.remove(aluno)
            print(f"\n Aluno(a) '{aluno['nome']}' removido com sucesso!")
            return 
            
    print(f"\n Aluno(a) '{nome_remover}' não encontrado.")

def calcular_media(lista_alunos):
    """Calcula e exibe a média geral das notas."""
    if not lista_alunos:
        print("\n📭 Não há alunos cadastrados para calcular a média.")
        return

    soma_notas = sum(aluno['nota'] for aluno in lista_alunos)
    media = soma_notas / len(lista_alunos)
    
    print(f"\n📊 A média geral de notas dos {len(lista_alunos)} alunos é: {media:.2f}")

def main():
    """Função principal que gerencia o fluxo do programa."""
    alunos = [] 
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-6): ").strip()
        
        if opcao == '1':
            adicionar_aluno(alunos)
        elif opcao == '2':
            listar_alunos(alunos)
        elif opcao == '3':
            buscar_aluno(alunos)
        elif opcao == '4':
            remover_aluno(alunos)
        elif opcao == '5':
            calcular_media(alunos)
        elif opcao == '6':
            print("\n Saindo do sistema... Até logo!")
            break
        else:
            print("\n Opção inválida! Por favor, escolha um número de 1 a 6.")


if __name__ == "__main__":
    main()