import os
clear = lambda: os.system('clear')
clear()

import random
from random import choices

print("Задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.")

def temp_name (number):
    match number:
        case 1:
            name = str('text_words.txt')
        case 2:
            name = str('text_code_words.txt')
        case _:
            name = str(input("Введите имя файла для записи: "))
    return name


def random_code (num, name_file_text):
    with open (name_file_text, "a", encoding="utf-8") as file_text:
        new_list_digit = choices (range(num*3), k=num)
        new_list_letter = choices ('qwertyuiopasdfghjklzxcvbnm', k=num)
        new_list = []
        for i in range (num):
            new_list.append(new_list_digit[i]*new_list_letter[i])
        
        any_string = ''.join(new_list)
        file_text.writelines(any_string)

def read_file (name_file):
    file = open(name_file, 'r')
    list_lines_file1 = file.readline()
    file.close()
    return list_lines_file1

def my_rle (name_file_text, name_file_code):
    any_string = read_file(name_file_text)
    with open (name_file_code, "a", encoding="utf-8") as code_text:
        count_digit = 1
        letter = any_string[0]
        code_list = []

        for i in range (1, len(any_string)):
            if any_string[i] == letter:
                count_digit = count_digit+1
                letter = any_string[i]
            else:
                code_list.append(str(count_digit))
                code_list.append(letter)
                count_digit = 1
                letter = any_string[i]
        
        if any_string[len(any_string)-1] == letter:
            code_list.append(str(count_digit))
            code_list.append(letter)
        
        code_string = ''.join(code_list)
        code_text.writelines(code_string)



def encode_string (name_file_code):
    any_string = read_file(name_file_code)
    code_string = list(any_string)
    digit = 0
    encode_list_digit = []
    encode_list_letter = []
    encode_list = []

    for i in range (len(code_string)):
        x = code_string[i]
        if x.isdigit():
            digit = digit*10 + int(x)
        else:
            encode_list_digit.append(digit)
            encode_list_letter.append(str(x))
            digit = 0
    
    for i in range (len(encode_list_digit)):
        encode_list.append(encode_list_digit[i]*encode_list_letter[i])
    
    encode_strig = ''.join(encode_list)
    return encode_strig

temp_name_number1 = int(input("Какое имя файла будем использовать для записи текста? 1 - text_words.txt, 3 - другое (ввести): "))
name_file_text = temp_name (temp_name_number1)

temp_name_number2 = int(input("Какое имя файла будем использовать для кодирования текста? 2 - text_code_words.txt, 3 - другое (ввести): "))
name_file_code = temp_name (temp_name_number2)

temp_name_number3 = int(input("Какой файл будем декодировать? 2 - text_code_words.txt, 3 - другое (ввести): "))
name_file_decode = temp_name (temp_name_number3)

num = int(input("Введите случайное целое число для генерации текста: "))
random_code (num, name_file_text)
my_rle (name_file_text, name_file_code)
print('\nСгенерированный и раскодированный текст:')
print(encode_string (name_file_decode))