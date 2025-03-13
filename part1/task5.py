import re


def words_with_a(user_string: str) -> str:
    """
    функция которая принимает строку и возвращает слова из этой строки
    начинающиеся на букву а/А
    :param user_string: строка от пользователя
    :return: str
    """
    words = re.findall(r"\b[аА]\w*", user_string)
    if words:
        print("Слова начинающиеся с буквы а:", words)
    else:
        print("Слов начинающихся с буквы а не найдено.")
    return words

if __name__ == "__main__":
    try:
        user_string = str(input("Введите строку:"))
        letter_a = words_with_a(user_string)
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Ошибка: {e}")
