# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
L = int (input("Введите длину шоколадки: "))
W = int (input("Введите ширину шоколадки: "))
K = int (input("Введите количество отламываемых долек: "))
if (K < L*W):
    if (K%L==0 or K%W==0):
        print ("Шоколадку можно разломить")
    else:
        print ("Отломить такую дольку сделав один разлом не получится")
else:
    print ("Отломить такую дольку сделав один разлом не получится")