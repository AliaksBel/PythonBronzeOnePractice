# Считываем входные данные
full_name = input()
surname, name, patronymic = full_name.split()

# Форматируем шапку таблицы
header = f"|{'ФАМИЛИЯ':>15}|{'ИМЯ':>15}|{'ОТЧЕСТВО':>15}|"

# Форматируем разделители
separator_top = "+---------------+---------------+---------------+"
separator_middle = "+===============+===============+===============+"
separator_bottom = "+---------------+---------------+---------------+"

# Форматируем данные с точками
#data = f"{surname.rjust(15, '.')} | {name.rjust(15, '.')} | {patronymic.rjust(15, '.')}"
width = 15
filler = '.'
result = f"|{surname:{filler}>{width}}|{name:{filler}>{width}}|{patronymic:{filler}>{width}}|"

# Заменяем разделители | на + в разделителях
header_formatted = header.replace('|', '|')
data_formatted = result.replace('|', '|')

# Выводим результат
print(separator_top)
print(header_formatted)
print(separator_middle)
print(data_formatted)
print(separator_bottom)

#OR

a,b,c = map(str, input().split())
print(f'''+---------------+---------------+---------------+
|        ФАМИЛИЯ|            ИМЯ|       ОТЧЕСТВО|
+===============+===============+===============+
|{a:.>15}|{b:.>15}|{c:.>15}|
+---------------+---------------+---------------+''')

#OR

a, b, c = input().split()

print(f'+{"":-<15}+{"":-<15}+{"":-<15}+')
print(f'|{"ФАМИЛИЯ":>15}|{"ИМЯ":>15}|{"ОТЧЕСТВО":>15}|')
print(f'+{"":=<15}+{"":=<15}+{"":=<15}+')
print(f'|{a:.>15}|{b:.>15}|{c:.>15}|')
print(f'+{"":-<15}+{"":-<15}+{"":-<15}+')