# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [1, 34, -10, 7, 6, -9, 57, 34, 56, 2, 1]

max = 20
min = 1

for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end = ' ')