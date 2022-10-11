# 3 Задайте последовательность чисел. 
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->
# [2, 4, 5, 9]

from random import randint


# in_lst = []
# for i in range(11):
#     in_lst.append(randint(0,10)) # добавляется новый элемент в список

in_lst = [1, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 8, 9, 10]
print(in_lst)

new_str = []
for i in in_lst:
    if in_lst.count(i) < 2:
        new_str.append(i)
print(new_str)       

            