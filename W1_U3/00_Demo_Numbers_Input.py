# Демо-файл: W1_U3/00_Demo_Numbers_Input.py

# 1. Получение данных от пользователя (это всегда строка!)
user_age_input = input("Введите ваш возраст: ")
item_price_input = input("Введите цену товара: ")

# 2. Преобразование типов (Type Casting)
# Мы должны явно превратить строки в числа для математики
try:
    user_age_int = int(user_age_input)
    item_price_float = float(item_price_input)

    # 3. Использование чисел в f-строках и расчетах
    print(f"Через 10 лет вам будет: {user_age_int + 10} лет.")

    # 4. Расчет с float
    tax_rate = 0.20  # 20% НДС
    tax_amount = item_price_float * tax_rate
    total_price = item_price_float + tax_amount

    print(f"Цена товара: {item_price_float}")
    print(f"НДС (20%): {tax_amount}")
    print(f"Итого к оплате: {total_price}")

except ValueError:
    # (Мы рассмотрим try/except подробнее позже,
    # но это базовая обработка ошибки, если пользователь ввел не число)
    print("Ошибка: Вы ввели не число!")