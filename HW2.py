time = int(input('введите время в секундах '))
hours = time // 3600 # узнаем сколько часов
total_seconds = time % 3600 # узнаем сколько еще осталось секунд
minutes = total_seconds // 60 # узнаем сколько минут
seconds = total_seconds % 60 # узнаем оставшиеся секунды

print(time,(f"секунд - это {hours}:{minutes}:{seconds}"))
