import json
import os


USER_DATA = {
        "name": input("Введите имя пользователя: "),
        "age": int(input("Введите возраст пользователя: ")),
        "city": input("Введите город пользователя: ")
}

def user_info(directory_name: str, file_path: str, user_data: dict) -> None:
    """
    функция создает директорию и файл формата json в ней
    для записи данных о пользователе
    :param directory_name: имя директории от пользователя
    :param user_data: данные о пользователе
    :param file_path: путь до файла
    :return: None
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Директория {directory_name} создана.")
    else:
        print(f"Директория {directory_name} существует.")

    with open(file_path, "w") as file:
        json.dump(user_data, file, ensure_ascii = False)

if __name__ == "__main__":
    try:
        directory_name = input("Введите имя директории:")
        file_path = os.path.join(directory_name, "user.json")
        user_info = user_info(directory_name, file_path, USER_DATA)
        print(f"Данные о пользователе были записаны в файл {file_path}")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Ошибка: {e}")