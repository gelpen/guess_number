from datetime import datetime

# Ваша строка с датой (в формате "ДД.ММ.ГГГГ")
date_string = "29.03.2024"

try:
    # Преобразуем строку в объект datetime
    date_object = datetime.strptime(date_string, "%d.%m.%Y")
    
    # Получаем номер дня недели (0 - понедельник, 6 - воскресенье)
    day_of_week = date_object.weekday()
    
    # Сопоставляем номер дня недели с его названием
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    day_name = days_of_week[day_of_week]
    
    print(f"Дата {date_string} - это {day_name}.")
except ValueError:
    print("Ошибка: неверный формат строки или недопустимые значения.")
