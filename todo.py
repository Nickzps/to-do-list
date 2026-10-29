import json
import os

FILE_NAME = 'tasks.json'

def load_tasks():
    """Загружает задачи из файла. Если файла нет, возвращает пустой список."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_tasks(tasks):
    """Сохраняет список задач в файл."""
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def show_tasks(tasks):
    """Выводит список всех задач на экран."""
    print("\n--- Ваш список задач ---")
    if not tasks:
        print("Задач пока нет. Отличный повод немного отдохнуть!")
        return
    
    for index, task in enumerate(tasks, 1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{index}. {status} {task['title']}")
    print("------------------------")

def add_task(tasks):
    """Добавляет новую задачу."""
    title = input("Введите название задачи: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print(f"Задача '{title}' добавлена!")
    else:
        print("Название не может быть пустым.")

def complete_task(tasks):
    """Отмечает задачу как выполненную."""
    show_tasks(tasks)
    try:
        task_num = int(input("Введите номер выполненной задачи: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['completed'] = True
            save_tasks(tasks)
            print("Отличная работа! Задача выполнена.")
        else:
            print("Такого номера нет в списке.")
    except ValueError:
        print("Пожалуйста, введите число.")

def delete_task(tasks):
    """Удаляет задачу из списка."""
    show_tasks(tasks)
    try:
        task_num = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Задача '{removed['title']}' удалена.")
        else:
            print("Такого номера нет в списке.")
    except ValueError:
        print("Пожалуйста, введите число.")

def main():
    """Главная функция с меню программы."""
    tasks = load_tasks()
    
    while True:
        print("\nМеню:")
        print("1. Посмотреть задачи")
        print("2. Добавить задачу")
        print("3. Отметить как выполненную")
        print("4. Удалить задачу")
        print("5. Выход")
        
        choice = input("Выберите действие (1-5): ").strip()
        
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()