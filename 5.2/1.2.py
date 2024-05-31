import re
import calendar

date = str(input("Введите дату в формате ГГГГ-ММ: "))


def calendarik(date):
    pattern = re.compile(r"\d{4}-\d{2}")
    if pattern.match(date):
        year, month = map(int, date.split("-"))
        cal = calendar.monthcalendar(year, month)
        for week in cal:
            print(week)
    else:
        print(
            "Указан неверный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ."
        )


calendarik(date)

phone_number = str(input("Введите номер телефона в формате +7-***-***-**-**: "))


def phone_number_check(phone_number):
    pattern = r"^(\+7|7|8)-\d{3}-\d{3}-\d{2}-\d{2}$"
    if re.match(pattern, phone_number):
        print(f"Номер телефона {phone_number} соответствует формату.")
    else:
        print(f"Номер телефона {phone_number} не соответствует формату.")


phone_number_check(phone_number)
