import json
import os

def user_info(directory_name: str, user_data: dict) -> None:
    """
    функция создает директорию и файл формата json в ней
    для записи данных о пользователе
    :param directory_name: имя директории от пользователя
    :param user_data: данные о пользователе
    :return: None
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Директория {directory_name} создана.")
    else:
        print(f"Директория {directory_name} существует.")

    

    file_path = os.path.join(directory_name, "user.json")

    with open(file_path, "w") as file:
        json.dump(user_data, file, ensure_ascii = False)

    print(f"Данные о пользователе были записаны в файл {file_path}")

if __name__ == "__main__":
    directory_name = input("Введите имя директории:")
    user_data = {
        "name": input("Введите имя пользователя: "),
        "age": int(input("Введите возраст пользователя: ")),
        "city": input("Введите город пользователя: ")
    }
    user_info = user_info(directory_name, user_data)