#N ребят делят K яблок поровну, неделящийся остаток остается в корзине. Сколько яблок достанется каждому ребенку?
#Сколько яблок останется в корзине? Программа получает на вход числа N и K на разных строках и должна вывести искомое
#количество яблок в отдельных строках.

n = int(input()) #к-во ребят
k = int(input()) #к-во яблок
print(k // n) #делим яблоки на ребят
print(k % n) #сколько яблок останется в корзине после дележки