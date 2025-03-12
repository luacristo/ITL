import os

directory_name = input("Введите имя директории:")
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    print(f"Директория {directory_name} создана.")
else:
    print(f"Директория {directory_name} существует.")

user_input = input("Введите строку:")
file_path = os.path.join(directory_name, "data.txt")

with open(file_path, "w") as file:
    file.write(user_input)

print(f"Строка записана в файл {file_path}")