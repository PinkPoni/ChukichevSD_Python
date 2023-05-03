# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
n_number = int(input("Введите количество элементов 1-го множества: "))
m_number = int(input("Введите количество элементов 2-го множества: "))
quantity_1 = []
quantity_2 = []
quantity_i = []
for i in range(n_number):
    n = int(input("Введите целое число 1-го множества: ")) # пользователь вводит целое число
    quantity_1.append(n) # сохранение элемента в конец списка
for i in range(m_number):
    m = int(input("Введите целое число 2-го множества: ")) # пользователь вводит целое число
    quantity_2.append(m) # сохранение элемента в конец списка
print(*quantity_1, sep=' ')
print(*quantity_2, sep=' ')
quantity_1m =set(quantity_1)
quantity_2m =set(quantity_2)
quantity_i = sorted(quantity_1m.intersection(quantity_2m))
print(*quantity_i, sep=' ')