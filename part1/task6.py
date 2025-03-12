import datetime
import time
def time_of_eternity() -> None:
    """
    функция которая выводит текущую дату и время,
    а также сколько секунд прошло с начала суток
    :return: None
    """
    current_datetime = datetime.datetime.now()
    print(f"Текущее время и дата {current_datetime}")

    current_time = time.time()
    seconds_since_midnight = current_time % 86400

    print(f"Секунд прошло с начала суток: {int(seconds_since_midnight)}")

if __name__ == "__main__":
    time_of_eternity()