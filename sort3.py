def quick_sort(arr) -> list[int]:
    """
    функция "быстрая сортировка"
    выбирает опорный элемент и сравнивает остальные элементы с ним для сортировки
    :return: list[int] (отсортированный список (массив))
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)