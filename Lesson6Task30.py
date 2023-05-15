# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
first_element = int(input("Введите первый элемент: "))
difference = int(input("Введите разность элементов: "))
count_elements = int(input("Введите количество элементов: "))

list = []
def list_progression(first_element, difference, count_elements):
    for i in range(1, count_elements+1):
        element = first_element + (i-1) * difference
        list.append(element)
    return list

print(*list_progression(first_element, difference, count_elements))