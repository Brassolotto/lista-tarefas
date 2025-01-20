
def mostrar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa encontrada!")
        return
    print("\n=== Lista de Tarefas ===")
    for i, tarefa in enumerate(tarefas, 1):
        status = "✓" if tarefa["concluida"] else " "
        print(f"{i}. [{status}] {tarefa['titulo']}")

