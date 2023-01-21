import os
clear = lambda: os.system('clear')
clear()

print("Задача 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.")

any_list = list((input ("Введите список (из примера): ")).replace(', ',' ').strip('[],').split(' '))
new_list = [any_list[x] for x in range(1,len(any_list)) if (int(any_list[x])>int(any_list[x-1]))]
print(new_list)
