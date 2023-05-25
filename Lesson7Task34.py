# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко 
# он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает 
# в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом 
# все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам  

text = input("Введите несколько слов (или фраз - слов разделенных дефисами): ")
# print(list(map(str,text.split())))
count_vowels = list(map(lambda x: sum(map(x.count,'aeiouаяуюоеёэиы')), list(map(str,text.split()))))
# print(count_vowels)
data = [obj for obj in range(len(count_vowels))]
res = list (map(lambda obj: count_vowels[obj] == count_vowels[0], data))
if all(res):
    print("Парам пам-пам")
else:
    print("Пам парам")