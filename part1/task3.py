import os
import random

def random_numbers(directory_name: str) -> None:
    """
    функция которая создает директорию с файлом
    и записывает в файл 5 рандомных чисел
    :param directory_name: имя директории передаваемое пользователем
    :return: None
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Директория {directory_name} создана.")
    else:
        print(f"Директория {directory_name} существует.")

    file_path = os.path.join(directory_name, "numbers.txt")

    with open(file_path, "w") as file:
        for i in range(5):  
            random_number = random.randint(1, 100)  
            file.write(f"{random_number}\n")

    print(f"5 рандомных чисел записаны в файл '{file_path}'.")

if __name__ == "__main__":
    directory_name = input("Введите имя директории:")
    random_numbers = random_numbers(directory_name)