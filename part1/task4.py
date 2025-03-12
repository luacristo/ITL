import os
import json

directory_name = input("Введите имя директории:")
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
    print(f"Директория {directory_name} создана.")
else:
    print(f"Директория {directory_name} существует.")

user_data = {
    "name": input("Введите имя пользователя: "),
    "age": int(input("Введите возраст пользователя: ")),
    "city": input("Введите город пользователя: ")
}

file_path = os.path.join(directory_name, "user.json")

with open(file_path, "w") as file:
    json.dump(user_data, file, ensure_ascii = False)

print(f"Данные о пользователе были записаны в файл {file_path}")