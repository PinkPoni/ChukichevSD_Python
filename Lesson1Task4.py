# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
S = int (input("Введите количество журавликов: "))
# S == P+K+C
# P == C
# K == P*4
P = S*2//3//4
k = P*4
K = S-P-P-k

print ("Петя и Сережа сделали по", P, "журавликов")
print ("Катя сделала в два раза больше, чем Петя и Сережа вместе -", k, "журавликов, плюс еще", K)