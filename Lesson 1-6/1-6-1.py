#Напишите программу, которая считает общее количество секунд, прошедших с начала суток до вводимого момента времени.

hours, minutes, seconds = map(int, input().split(':'))
print((hours * 3600) + (minutes * 60) + seconds)