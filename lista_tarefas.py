
def mostrar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa encontrada!")
        return
    print("\n=== Lista de Tarefas ===")
    for i, tarefa in enumerate(tarefas, 1):
        status = "✓" if tarefa["concluida"] else " "
        print(f"{i}. [{status}] {tarefa['titulo']}")

def main():
    tarefas = []

    while True:
        print("\n=== Menu ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        opcao = input("\nEscolha uma opção (1-5): ")

        if opcao == "1":
            titulo = input("Digite o título da tarefa: ")
            tarefas.append({"titulo": titulo, "concluida": False})
            print("Tarefa adicionada com sucesso!")

        elif opcao == "2":
            mostrar_tarefas(tarefas)

        elif opcao == "3":
            mostrar_tarefas(tarefas)
            try:
                indice = int(input("\nDigite o número da tarefa a ser concluída: ")) - 1
                if 0 <= indice < len(tarefas):
                    tarefas[indice]["concluida"] = True
                    print("Tarefa marcada como concluída!")
                else:
                    print("Número de tarefa inválido!")
            except ValueError:
                print("Por favor, digite um número válido!")

        elif opcao == "4":
            mostrar_tarefas(tarefas)
            try:
                indice = int(input("\nDigite o número da tarefa a ser removida: ")) -1
                if 0 <= indice < len(tarefas):
                    tarefas.pop(indice)
                    print("Tarefa removida com sucesso!")
                else:
                    print("Número de tarefa inválido!")
            except ValueError:
                print("Por favor, digite um número válido!")

        elif opcao =="5":
            print("\nObrigado por usar a Lista de Tarefas!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()