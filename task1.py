# 1 Вычислить число π c заданной точностью d
# *Пример:* 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# https://completerepair.ru/kak-vychislit-chislo-pi

from operator import truediv


accuracy_in = input("Введите точность с которой надо вычислить число π \n")
n = 1

sum_pi = 0

for i in range(1000000):
    sum_pi += 1/((2*i+1)*(-1)**i)
    i +=1
    
accuracy = len(accuracy_in)

print(str(4*sum_pi)[: accuracy])
