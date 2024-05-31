days_of_week = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]

days = {index + 1: day for index, day in enumerate(days_of_week)}

print(days)
