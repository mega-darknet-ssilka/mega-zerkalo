from datetime import datetime

# Запрашиваем имя
name = input("Как тебя зовут? ")

# Получаем текущую дату
now = datetime.now()
date_str = now.strftime("%d %B %Y года, %A")

# Приветствие
print(f"\nПривет, {name}! 👋")
print(f"Сегодня {date_str}.")
print("Желаю тебе хорошего дня! 🌟")
