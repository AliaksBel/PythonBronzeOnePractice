str_data_1 = 'Hello happy world'
word_11, word_12, word_13 = str_data_1.split()
print(word_11)
print(word_12)
print(word_13)


str_data_2 = 'Hello--happy--world'
word_21, word_22, word_23 = str_data_2.split('--')
print(word_21)
print(word_22)
print(word_23)

width, number, filler = input().split()
width = int(width)
number = int(number)
print(f'{number:{filler}>{width}}')

int_1, int_2, int_3 = map(int, input().split())
print(int_1, int_2, int_3)
print(type(int_1), type(int_2), type(int_3))