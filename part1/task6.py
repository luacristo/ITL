import datetime
import time

current_datetime = datetime.datetime.now()
print(f"Текущее время и дата {current_datetime}")

current_time = time.time()
seconds_since_midnight = current_time % 86400

print(f"Секунд прошло с начала суток: {int(seconds_since_midnight)}")