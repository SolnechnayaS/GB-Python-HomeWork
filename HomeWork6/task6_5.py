import os
clear = lambda: os.system('clear')
clear()

from random import sample
import random

print("Задача 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого).")
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
nouns =list(str(input("Введите через запятую все существительные: ")).strip('[]').split(','))
adverbs =list(str(input("Введите через запятую все наречия: ")).strip('[]').split(','))
adjectives =list(str(input("Введите через запятую все прилагательные: ")).strip('[]').split(','))
num_word = int(input("Введите число шуток: "))

while num_word > len(nouns)*len(adverbs)*len(adjectives):
    num_word = int(input(f"Шутки не будут уникальными, введите число меньше {len(nouns)*len(adverbs)*len(adjectives)}: "))

def list_joke (num_word, nouns, adverbs, adjectives):
    list_index = []
    for i in range(len(nouns)):
        for j in range(len(adverbs)):
            for k in range(len(adjectives)):
                list_index.append([i,j,k])

    new_list = sample (list_index, k=num_word)
    list_joke = []
    for i in range (len(new_list)):
        temp_string = str(nouns[int(new_list[i][0])] + " " + adverbs[int(new_list[i][1])] + " " + adjectives[int(new_list[i][2])])
        list_joke.append(temp_string)

    return list_joke

print (", ".join(list_joke(num_word, nouns, adverbs, adjectives)))
