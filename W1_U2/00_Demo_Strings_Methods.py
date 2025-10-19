# Демо-файл: 00_Demo_Strings_Methods.py

# 1. Объявление переменных
dev_name = "максим"
dev_skill = "PYTHON"

# 2. Использование f-строк и методов
# .title() делает первую букву заглавной
# .lower() делает все буквы маленькими
# .strip() удаляет пробелы в начале и конце
message = (f"Разработчик: {dev_name.title()} "
           f"использует язык {dev_skill.lower()}")

# 3. Демонстрация метода .strip()
city_input = " \n москва \t "
city_clean = city_input.strip()

print(message)
print(f"Город до очистки: '{city_input}'")
print(f"Город после очистки: '{city_clean}'")