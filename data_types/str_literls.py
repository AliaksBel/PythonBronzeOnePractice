my_str_1 = 'Это простой литерал str'
my_str_2 = "А это еще один литерал str"
print(my_str_1)
print(my_str_2)

my_multiline_str_1 = '''А это
многострочный литерал.
Иногда бывает полезен.'''
my_multiline_str_2 = """Так
тоже можно"""
print(my_multiline_str_1)
print(my_multiline_str_2)

#r-литералы
my_raw_str_1 = r'Raw литерал не поддерживает экранирование: \t\n'
my_raw_str_2 = r'''Многострочный
Raw литерал:\t\n\\'''
print(my_raw_str_1)
print(my_raw_str_2)

#b-литералы
my_byte_str_1 = b'Byte literal supports only ascii'
my_byte_str_2 = b'''Multiline
byte literal'''
print(my_byte_str_1)
print(my_byte_str_2)

hello = '\x48\x65\x6c\x6c\x6f'
print(hello)

#f-литералы
int_var = 100
float_far = 2.34567
my_formatted_str = f'Это отформатированная строка.\nЗдесь будет ЗНАЧЕНИЕ переменной int_var {int_var}\nА здесь - значение переменной float_far {float_far:.2f}'
print(my_formatted_str)

print(f'{42:<5}')
print(f'{42:>5}')
width = 10
filler = '.'
print(f'{42:*<{width}}')
print(f'{42:{filler}>{width}}' f'{42:{filler}>{width}}')


data = 100
f_str_1 = f'''Эти скобки {{ data }} - просто скобки
А эти {data} - для вычисления выражения'''
print(f_str_1)