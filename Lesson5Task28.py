# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4 
a = int(input("Введите первое число (неотрицательное, целое): "))
b = int(input("Введите второе число (неотрицательное, целое): "))
def sumNumbers(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return sumNumbers(a+1,b-1)
print(sumNumbers(a, b))