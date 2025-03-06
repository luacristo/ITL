from sort1 import bubble_sort
from sort2 import selection_sort
from sort3 import quick_sort

def main() -> None:
    """
    основная функция где вызываются все сортировки
    :return: None
    """
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный список:", data)
    try:
      result = bubble_sort(data.copy())
      print("Сортировка пузырьком:", result)
      result2 = selection_sort(data.copy())
      print("Сортировка выбором:", result2)
      result3 = quick_sort(data.copy())
      print("Быстрая сортировка:", result3)
    except Exception as e:
      print("Ошибка в сортировке", e)

if __name__ == "__main__":
  main()
