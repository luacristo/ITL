import math


def calculations(user_number: int) -> tuple[float, int]:
    """
    функция которая высчитывает корень и факториал числа
    :param user_number: число которое передает пользователь
    :return: tuple[float, int]
    """
    if user_number < 0:
        raise ValueError("Введите положительно число")

    sqrt_number = math.sqrt(user_number)
    factorial_number = math.factorial(user_number)
    return sqrt_number, factorial_number

if __name__ == '__main__':
    try:
        user_number = int(input("Введите целое число:"))
        sqrt_number, factorial_number = calculations(user_number)
        print(f"Корень числа равен: {sqrt_number}, факториал числа равен: {factorial_number}")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Ошибка: {e}")