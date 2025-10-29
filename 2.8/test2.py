surname = input()
name = input()
patronymic = input()

result = f"{'.'*9}{surname} {'.'*9}{name} {'.'*8}{patronymic}"
print(result)


surname = input()
name = input()
patronymic = input()
width = 15
filler = '.'
result = f"'{surname:{filler}>{width}}' '{name:{filler}>{width}}' '{patronymic:{filler}>{width}}'"
print(result)