def bubble_sort(arr: list[int]) -> list[int]:
    """
    функция "сортировка пузырьком"
    последовательно сравнивает значения ближайших элементов и меняет их местами,
    если предыдущее оказывается больше следующего
    :param arr: list[int]: массив целых чисел для сортировки
    :return: list[int] (отсортированный список (массив))
    """
    n = len(arr)
    swapped = False
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr