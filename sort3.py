def quick_sort(arr: list[int]) -> list[int]:
    """
    функция "быстрая сортировка"
    выбирает опорный элемент и сравнивает остальные элементы с ним для сортировки
    :param arr: list[int]: массив целых чисел для сортировки
    :return: list[int] (отсортированный список (массив))
    """
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    pivot = sorted([arr[0], arr[middle], arr[-1]])[1]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + equal + quick_sort(right)