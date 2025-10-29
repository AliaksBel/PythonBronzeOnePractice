# Получаем ввод от пользователя
input_value = input().strip()

# Определяем систему счисления входного значения
if input_value.startswith('0b'):
    # Если это бинарное число
    base = 2
else:
    # Иначе предполагаем десятичное число
    base = 10

# Преобразуем ввод в целое число с учетом системы счисления
int_value = int(input_value, base)

# Преобразуем в строки
dec_str_value = str(int_value)
bin_str_value = bin(int_value)

# Выводим результаты
print(f"Исходное значение: {input_value}")
print(f"Десятичное представление: {dec_str_value}")