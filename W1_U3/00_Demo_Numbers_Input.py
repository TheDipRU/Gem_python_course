# Демо-файл: W1_U3/00_Demo_Numbers_Input.py

# 1. Получение данных (Ввод всегда возвращает строку)
user_age_str = input("Введите ваш возраст: ")
item_price_str = input("Введите цену товара: ")

# 2. Преобразование типов и демонстрация операторов
try:
    # Преобразуем ввод в int и float
    user_age = int(user_age_str)
    item_price = float(item_price_str)

    # 3. Расчет: сложение, использование больших чисел
    future_age = user_age + 10
    total_revenue = 1_500_000  # Читабельное int

    # 4. Расчет: деление и остаток
    hours = 150
    calc_hours = hours // 60
    calc_minutes = hours % 60

    print(f"Через 10 лет вам будет: {future_age} лет.")
    print(f"Итоговая стоимость (с НДС 20%): {item_price * 1.20:.2f}") # {:.2f} - форматирование float
    print(f"150 минут - это: {calc_hours} ч. {calc_minutes} мин.")

except ValueError:
    # Мы рассмотрим это позже, но это защита, если пользователь введет "привет" вместо числа.
    print("Ошибка ввода: Введите числовое значение.")