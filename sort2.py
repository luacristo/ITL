def selection_sort(arr: list[int]) -> list[int]:
    """
    функция "сортировка выбором" 
    проходит по списку выбирает минимальный элемент и смещает его в начало
    :param arr: list[int]: массив целых чисел для сортировки
    :return: list[int] (отсортированный список (массив))
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr