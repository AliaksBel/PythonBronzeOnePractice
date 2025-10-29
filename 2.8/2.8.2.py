surname = input()
name = input()
patronymic = input()
width = 15
filler = '.'
result = f"{surname:{filler}>{width}} {name:{filler}>{width}} {patronymic:{filler}>{width}}"
print(result)

#OR

a = input()
b = input()
c = input()
print(f'{a:.>15}', f'{b:.>15}', f'{c:.>15}')
