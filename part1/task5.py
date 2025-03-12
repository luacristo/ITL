import re

user_string = str(input("Введите строку:"))
words = re.findall(r"\b[аА]\w*", user_string)
if words:
    print("Слова начинающиеся с буквы а:", words)
else:
    print("Слов начинающихся с буквы а не найдено.")