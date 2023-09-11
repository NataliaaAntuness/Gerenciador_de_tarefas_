class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        if self.tasks:
            print("Tarefas pendentes:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Nenhuma tarefa pendente.")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            print(f"Tarefa concluída: {task}")
            self.tasks.pop(task_index - 1)
        else:
            print("Índice de tarefa inválido.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nOpções:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            task = input("Digite a tarefa: ")
            task_manager.add_task(task)
        elif choice == "2":
            task_manager.list_tasks()
        elif choice == "3":
            task_index = int(input("Digite o índice da tarefa concluída: "))
            task_manager.mark_task_completed(task_index)
        elif choice == "4":
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()