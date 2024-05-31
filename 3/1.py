def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return x / y


def power(x, y):
    return x**y


def validate_input(value):
    try:
        return float(value)
    except ValueError:
        raise ValueError("Неверный ввод. Введите числовое значение.")


def calculator():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Выход")

        choice = input("Введите номер операции (1/2/3/4/5/6): ")

        if choice == "6":
            print("Выход из программы")
            break

        if choice in ["1", "2", "3", "4", "5"]:
            try:
                num1 = validate_input(input("Введите первое число: "))
                num2 = validate_input(input("Введите второе число: "))

                if choice == "1":
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == "2":
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                elif choice == "5":
                    print(f"{num1} ^ {num2} = {power(num1, num2)}")

            except ValueError as ve:
                print(ve)
            except ZeroDivisionError as zde:
                print(zde)
        else:
            print("Неверный выбор. Пожалуйста, выберите операцию из списка.")


if __name__ == "__main__":
    calculator()
