#Задача 3
def pascal_row(n):
    row = [1]
    for _ in range(n):
        row = [x + y for x, y in zip([0] + row, row + [0])]
    return row

print(pascal_row(4))
