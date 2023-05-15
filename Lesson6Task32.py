# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random
quantity = int(input("Введите количество элементов в массиве: "))
min_element = int(input("Введите минимальное значение числа: "))
max_element = int(input("Введите максимальное значение числа: "))

# Создаем рандомный список
n_number = []
for i in range(quantity):
    temp = random.randint(-10, 10) # Числа ограничены значением 10 для упрощения, можно задать любое значение
    n_number.append(temp)
print (*n_number, sep=' ') # Выводим сгенерированный список без скобок и запятых 

list_result = []

def list_selection(min_element, max_element):
    for i in range(len(n_number)):
        if n_number[i] >= min_element and n_number[i] <= max_element:
            list_result.append(i)
    return list_result

print(list_selection(min_element, max_element))