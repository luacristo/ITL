def add_task():
    """
    Эта функция добавляет новую задачу в список задач
    Запрашивает у пользователя данные: название, описание и приоритет задачи от одного до 5
    """
    title = str(input("Введите название: "))
    description = str(input("Введите описание: "))

    while True:
        priority = int(input("Введите приоритет (1 - 5): "))
        if 1 <= priority <= 5:
            break
        print("Ошибка: приоритет должен быть от 1 до 5. \n")

    task = {"title": title, "description": description, "priority": priority}
    return task

tasks = [] 

def view_tasks():
    """
    Эта функция выводит список всех задач, которые отсортированы по приоритету задачи (от наибольшего к меньшему)
    Также позволяет пользователю выбрать, вывести все задачи или только первые 5

    """
    if not tasks:
        print("Список пуст \n")
        return

    sorted_tasks = sorted(tasks, key=lambda x: x["priority"], reverse=True)

    user_choice = input("Выберите количество задач для просмотра первые 5 или все (5 or all): ")
    if user_choice == "5":
        sorted_tasks = sorted_tasks[:5]
    for index, task in enumerate(sorted_tasks, start=1):
            print(f"{index}. {task['title']} - {task['description']} (Приоритет: {task['priority']}) \n")
    
def edit_task():
    """
    Эта функция позволяет пользователю редактировать уже созданную задачу
    Можно изменить название, описание или приоритет задачи, также можно оставить поле пустым, чтобы значение не поменялось
    """
    if not tasks:
        print("Список пуст \n")
        return

    view_tasks()
    
    task_number = int(input("Введите номер задачи: \n ")) - 1
    if not (0 <= task_number < len(tasks)):
        print("Ошибка: некорректный номер задачи. \n ")
        return

    task = tasks[task_number]

    new_title = str(input("Введите новое название (оставьте поле пустым, чтобы сохранить старое): "))
    new_description = str(input("Введите новое описание (оставьте поле пустым, чтобы сохранить старое): "))

    while True:
        new_priority = int((input("Введите новый приоритет (1 - 5, оставьте поле пустым, чтобы сохранить старое): ")))
        if new_priority == "":
            break
        if 1 <= new_priority <= 5:
            new_priority = int(new_priority)
            break
        print("Ошибка: приоритет должен быть от 1 до 5. \n")
    if new_title:
        task["title"] = new_title
    if new_description:
        task["description"] = new_description
    if new_priority:
        task["priority"] = int(new_priority)

    print("Задача успешно обновлена. \n")

def delete_task():
    """
    Эта функция позволяет пользователю удалить выбранную задачу
    """
    if not tasks:
        print("Список пуст \n")
        return

    view_tasks()
    
    task_number = int(input("Введите номер задачи: ")) - 1
    if not (0 <= task_number < len(tasks)):
        print("Ошибка: некорректный номер задачи. \n")
        return

    del tasks[task_number]
    print("Задача успешно удалена. \n")

def main_menu():
    """
    Это главное меню программы, позволяет пользователю полностью управлять программой
    А также выбрать одно из пяти действий
    """
    while True:
        print("1. Добавить задачу\n"
              "2. Просмотреть задачи\n"
              "3. Редактировать задачу\n"
              "4. Удалить задачу\n"
              "5. Выйти\n")

        user = int(input("Что вы хотите сделать? (1 - 5): "))
        
        if user < 1 or user > 5:
            print("Ошибка: введите число от 1 до 5. \n")
            continue
        
        if user == 5:
            break
        elif user == 1:
            tasks.append(add_task())
        elif user == 2:
            view_tasks()
        elif user == 3:
            edit_task()
        elif user == 4:
            delete_task()

main_menu()