#Напишите программу, которая выводит сумму двух целых чисел, заданных в одной строке через пробел.

a, b = input().split()
a, b = int(a), int(b)
print(a + b)