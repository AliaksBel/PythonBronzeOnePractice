# Различные способы преобразовать объект int в объект str

int_value = 1000

dec_str_value = str(int_value)
print('Значение в десятичной:', dec_str_value)
print('Тип:', type(dec_str_value))

hex_str_value = hex(int_value)
print('Значение в шестнадцатеричной:', hex_str_value)
print('Тип:', type(hex_str_value))

oct_str_value = oct(int_value)
print('Значение в восмеричной:', oct_str_value)
print('Тип:', type(oct_str_value))

bin_str_value = bin(int_value)
print('Значение в двоичной:', bin_str_value)
print('Тип:', type(bin_str_value))