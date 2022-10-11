# 4 Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в 
# файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }


def degree(digit: int, deg: int):
    degrees = ""
    temp = str(deg)
    for char in temp:
        degrees += indexes[char] or ""
    return str(digit) + degrees

k = int(input("Введите число \n"))
deg = k+1
in_lst = []

with open('file', 'w', encoding='utf-8') as f:
    for i in range(k+1):
        s_d = str(degree("x",deg))
        if i>0:
            if deg > 1:
                s = str(randint(0,100)) + s_d
            else:
                s = str(randint(0,100)) + "x"
            f.write(s)
        if i !=k and i !=0 :
            f.write("+")
        if i == k:
            s = str(randint(0,100)) + " = 0"
            f.write("+")
            f.write(s)
        deg-=1 
        
with open('file', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(lines)