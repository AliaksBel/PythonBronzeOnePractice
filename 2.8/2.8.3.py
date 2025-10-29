# Чтение входных данных
numbers = input().split()     # получаем список строк с числами
separator = input()           # получаем разделитель

# Преобразование элементов списка в целые числа и увеличение каждого на 1
increased_numbers = [int(num) + 1 for num in numbers]

# Преобразование полученных чисел обратно в строки
string_numbers = map(str, increased_numbers)

# Объединение чисел с использованием указанного разделителя
result_string = separator.join(string_numbers)

# Вывод результата
print(result_string)

#OR
a, b, c = input().split()
a = int(a) + 1
b = int(b) + 1
c = int(c) + 1
separ = input()
print(a, b, c, sep=separ)

#OR

a, b, c = map(lambda x: int(x) + 1, input().split())
s = input()
print(a, b, c, sep=s)