import os

def create_directory(directory_name: str, user_input: str) -> None:
    """
    функция создает директорию в этой директории создается файл
    в этот файл записывается строка которая была введена пользователем
    :param directory_name: имя директории для создания
    :return: None
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Директория {directory_name} создана.")
    else:
        print(f"Директория {directory_name} существует.")
        raise ValueError('Недопустимое значение')

    file_path = os.path.join(directory_name, "data.txt")

    encoding = str(input("Введите желаемую кодировку (например, utf-8, windows-1251):"))

    try:
        with open(file_path, "w", encoding=encoding) as file:
            file.write(user_input)
        print(f"Строка записана в файл {file_path}, с кодировкой {encoding}")
    except ValueError:
        print(f"Ошибка: кодировка {encoding} не поддерживается")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    directory_name = input("Введите имя директории:")
    user_input = input("Введите строку:")
    file_path = create_directory(directory_name, user_input)