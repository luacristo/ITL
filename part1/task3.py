import os
import random


def random_numbers(directory_name: str, file_path: str) -> None:
    """
    функция которая создает директорию с файлом
    и записывает в файл 5 рандомных чисел
    :param directory_name: имя директории передаваемое пользователем
    :param file_path: путь до файла
    :return: None
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Директория {directory_name} создана.")
    else:
        print(f"Директория {directory_name} существует.")

    with open(file_path, "w") as file:
        for i in range(5):  
            random_number = random.randint(1, 100)  
            file.write(f"{random_number}\n")

if __name__ == "__main__":
    try:
        directory_name = input("Введите имя директории:")
        file_path = os.path.join(directory_name, "numbers.txt")
        random_numbers = random_numbers(directory_name, file_path)
        print(f"5 рандомных чисел записаны в файл '{file_path}'.")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Ошибка: {e}")