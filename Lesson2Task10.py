# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# Пример: 
# 5 -> 1 0 1 1 0
# 2
import random
n_coins = int(input("Введите количество монеток: "))
n_0 = 0
n_1 = 0
for i in range(n_coins):
    temp = random.randint(0, 1)
    print (i, temp)
    if temp == 0:
        n_0 += 1
n_1 = n_coins - n_0
if n_1 < n_0:
    n_min = n_1
else:
    n_min = n_0
print("Минимальное количество монет, котрые нужно перевернуть: ", n_min)