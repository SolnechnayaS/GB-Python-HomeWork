# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

import os
clear = lambda: os.system('clear')
clear()

import random
from random import sample

print("Задача 1. Напишите программу, удаляющую из текста все слова, содержащие 'абв'. В тексте используется разделитель пробел.")

def new_list_string ():
    num = int(input("Введите количество слов для генерации случайной строки: "))
    text_temp = str(input("Введите символы для генерации случайных слов (и удаления этой последовательности): "))
    new_list = []
    for i in range (num):
        text = sample (text_temp, k=len(text_temp))
        new_list.append(''.join(text))
    print(' '.join(new_list))
    
    new_list2 = new_list.copy()
    if text_temp not in new_list2:
        print(f'Сгенерированный список не содержит значение: {text_temp}')
    else:
        while text_temp in new_list2:
            new_list2.remove(text_temp)
        print(' '.join(new_list2))

new_list_string()