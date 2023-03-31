# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

from random import randint

a = int(input("Укажите начальное значение диапазона: "))
b = int(input("Укажите конечное значение диапазона: "))

n = int(input("Укажите размерность массива: "))
arr = [randint(-10,10) for _ in range(n)]
print(arr)
print()

new_arr_index = []
new_arr_element = []
for i in range(n):
    if a < arr[i] < b:
        new_arr_element.append(arr[i])
        new_arr_index.append(i)

print(new_arr_element)
print(new_arr_index)