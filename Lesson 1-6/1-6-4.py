#Подсчитайте для студента среднее арифметическое всех оценок, полученных за три месяца учёбы. Входные данные
#представлены в одной строке и разделены точкой с запятой - три оценки и фамилия студента. Вывод осуществить в одну
#строку через пробел, сначала фамилия, потом средняя оценка.

a, b, c, s = input().split(';')
a, b, c = float(a), float(b), float(c)
print(s, ((a + b + c) / 3))